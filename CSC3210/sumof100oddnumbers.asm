.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
.code
main PROC
mov eax, 1
mov ebx, 1
mov ecx, 99
L1:
	add ebx, 2
	add eax, ebx
	loop L1
invoke ExitProcess,0
main endp
end main
