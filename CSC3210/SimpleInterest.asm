.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
.code
main PROC
mov eax, 1011
mov ebx, 2
mov edx, 50
imul eax, ebx
mov bx, 100
imul eax, edx
sub edx, edx
idiv bx
invoke ExitProcess,0
main endp
end main
