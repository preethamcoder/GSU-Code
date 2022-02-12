;Name Preetham Thelluri
;Class: CSC3210
;Assignment#: 3
;Description: This program attempts to reverse the elements inside a string array with loop and xchg instructions.
.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
inputStr BYTE "A", "B", "C", "D", "E", "F", "G", "H"
.code
main proc
mov edi, OFFSET inputStr
add edi, 7
mov ebx, OFFSET inputStr
mov ecx, 4
L1:
	mov al, [edi]
	xchg [ebx], al
	xchg al, [edi]
	inc ebx
	dec edi
	LOOP L1
invoke ExitProcess,0
main endp
end main
