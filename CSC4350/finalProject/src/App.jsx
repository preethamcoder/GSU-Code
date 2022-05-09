import './App.css';
import React, { useState, useEffect } from 'react';
import YouTube from 'react-youtube';
import { ReactComponent as Search } from './images/search.svg';
import { ReactComponent as Skip } from './images/skip.svg';
import { ReactComponent as Comment } from './images/comment.svg';
import { ReactComponent as Save } from './images/save.svg';

const API_KEY = process.env.REACT_APP_YT_KEY;
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/';

function App() {
  const [initalId, setInitalId] = useState('');
  const [videoIds, setVideoIds] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [query, setQuery] = useState('');
  const [enterFlag, setEnterFlag] = useState(false);
  const [videoListIndex, setVideoListIndex] = useState(-1);
  const [videoComments, setVideoComments] = useState([]);
  const [userLoggedIn, setUserLoggedIn] = useState(false);
  const [savedPlaylists, setSavedPlaylists] = useState([]);

  // get initial video id based on query
  useEffect(() => {
    if (!enterFlag) return;
    const params = {
      part: 'snippet',
      key: API_KEY,
      q: query,
      type: 'video',
    };
    fetch(`${YOUTUBE_URL}search?part=${params.part}&q=${params.q}&maxResults=10&key=${params.key}`, {
      // for local testing to save api calls (files located in public folder)
      // fetch('./static/react/searchreturn.json', {
      // fetch('./static/react/searchreturn_firstitemchannel.json', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    }).then((response) => response.json()).then((data) => {
      // get first item with video id
      let foundFlag = false;
      for (let i = 0; i < data.items.length; i += 1) {
        if (data.items[i].id.kind === 'youtube#video') {
          foundFlag = true;
          setInitalId({
            id: data.items[i].id.videoId,
            title: data.items[i].snippet.title,
          });
          break;
        }
      }
      if (!foundFlag) alert('No Videos Found Based on Search Parameters');
    });
  }, [query]);

  // get list of related videos based on initial video id
  useEffect(() => {
    if (!enterFlag) return;
    const params = {
      part: 'snippet',
      key: API_KEY,
      numResults: 20,
      videoId: initalId.id,
      type: 'video',
    };

    fetch(`${YOUTUBE_URL}search?part=${params.part}&relatedToVideoId=${params.videoId}&maxResults=${params.numResults}&type=${params.type}&key=${params.key}`, {
      // for local testing to save api calls (files located in public folder)
      // fetch('./static/react/relatedreturn.json', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
    }).then((response) => response.json()).then((data) => {
      const newIds = [initalId];
      data.items.forEach((item) => {
        if (item.hasOwnProperty.call(item, 'snippet')) {
          newIds.push({
            id: item.id.videoId,
            title: item.snippet.title,
          });
        }
      });
      setVideoIds(newIds);
    });
    setEnterFlag(false);
  }, [initalId]);

  // set video index when videoIds is updated
  useEffect(() => {
    if (videoIds.length === 0) return;
    setVideoListIndex(0);
  }, [videoIds]);

  // get comments for currently playing video
  useEffect(() => {
    // TODO: remove try catch when backend is set up
    if (videoListIndex === -1) return;
    try {
      fetch(`/getComments?videoId=${videoIds[videoListIndex].id}`)
        .then((response) => response.json())
        .then((data) => {
          setVideoComments(data.comment_list);
        });
    } catch (err) {
      console.log('An Error Occured: ', err);
    }
  }, [videoListIndex, videoIds]);

  // get if user is logged in
  useEffect(() => {
    fetch('/userLoggedIn')
      .then((response) => response.json())
      .then((data) => {
        setUserLoggedIn(data.logged_in);
      });
  }, []);

  // get saved playlists
  useEffect(() => {
    fetch('/getPlaylist')
      .then((response) => response.json())
      .then((data) => {
        setSavedPlaylists(data.savedPlaylists);
      });
  }, []);

  const savePlaylist = () => {
    const newSaveObj = {
      title: query,
      playlist: JSON.stringify(videoIds),
    };

    console.log('newSaveObj: ', newSaveObj);
    fetch('/addPlaylist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newSaveObj),
    }).then((response) => response.json()).then((data) => {
      console.log(data);
      setSavedPlaylists(data.savedPlaylists);
      console.log('savedPlaylists: ', savedPlaylists);
    });
  };

  const onSearchClick = (e) => {
    e.preventDefault();
    setQuery(inputValue);
    setEnterFlag(true);
    setInputValue('');
  };

  const updateFieldChanged = (e) => {
    setInputValue(e.target.value);
  };

  const playNext = () => {
    if (videoListIndex === videoIds.length - 1) {
      alert('end of playlist, starting over');
      setVideoListIndex(0);
    } else {
      setVideoListIndex(videoListIndex + 1);
    }
  };

  // add comment to database for currently playing video
  const addComment = () => {
    const newCommentObj = {
      videoId: videoIds[videoListIndex].id,
      videoTitle: videoIds[videoListIndex].title,
      comment: inputValue,
    };

    // TODO: remove try catch when backend is set up
    try {
      fetch('/addComment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newCommentObj),
      }).then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (!userLoggedIn) {
            alert('User Must be logged in to perform this action');
          } else {
            setVideoComments(data.comment_list);
          }
        });
    } catch (err) {
      console.log('Error adding comment: ', err);
    }
    setInputValue('');
  };

  // TODO: style
  return (
    <div>
      <div>
        <div className="nav">
          {userLoggedIn ? (
            <a className="remove-highlighting" href="/logout"> LOGOUT</a>
          ) : (
            <a className="remove-highlighting" href="/login">LOGIN</a>
          )}
        </div>
        <div className="App">
          {videoIds.length === 0
            && (
              <h3 className="description">
                Search for your favorite artist, song,
                or content creator to get an automatically generated playlist
              </h3>
            )}
          <form onSubmit={onSearchClick}>
            <input className="search-bar" type="text" placeholder="Search" onChange={updateFieldChanged} />
            <button type="button" onClick={onSearchClick} className="search-button">
              <Search />
            </button>
          </form>
        </div>
        <div>
          {videoIds.length > 0 && videoListIndex !== -1
            && (
              <div>
                <h3>{videoIds[videoListIndex].title}</h3>
                <YouTube
                  className="video"
                  videoId={videoIds[videoListIndex].id}
                  opts={{
                    playerVars: {
                      autoplay: 1,
                    },
                  }}
                  onEnd={playNext}
                />
                <button type="button" onClick={playNext} className="skip-button">
                  <Skip />
                </button>
                {userLoggedIn && (
                  <button className="save-button" type="button" onClick={savePlaylist}>
                    <Save />
                  </button>
                )}
              </div>
            )}
        </div>
        <div className="comment-wrapper">
          {videoIds.length > 0
            && videoListIndex !== -1
            && (
              <div>
                <div>
                  <input
                    className="input"
                    placeholder={userLoggedIn ? 'Leave a Comment' : 'Must Be Logged in to Leave A Comment'}
                    onChange={updateFieldChanged}
                  />
                </div>
                <br />
                <button type="button" onClick={(addComment)} className="skip-button">
                  <Comment className="comment-button" />
                </button>
              </div>
            )}
        </div>
        <div>
          {/* Comments: */}
          <br />
          {videoComments
            && videoComments.length > 0
            && videoComments.map((comment) => (
              <div>
                <div className="comments">
                  <div className="username">
                    {comment.user}
                  </div>
                  {comment.text}
                </div>
                <br />
              </div>
            ))}
        </div>
      </div>
      <div style={{
        position: 'fixed',
        right: '5%',
        top: '25%',
      }}
      >
        {userLoggedIn && savedPlaylists.length > 0 && (
          <div>
            <h3>Your Saved Playlists:</h3>
            <ul>
              {savedPlaylists.map((playlist) => (
                <li style={{
                  'list-style-type': 'none',
                  'text-align': 'right',
                  'line-height': '1.6',
                }}
                >
                  <button
                    className="remove-highlighting"
                    type="button"
                    onClick={() => setVideoIds(JSON.parse(playlist.playlist))}
                  >
                    {playlist.playlistTitle}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
