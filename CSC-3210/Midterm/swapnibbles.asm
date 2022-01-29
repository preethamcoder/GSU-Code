.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
.code
main PROC
	mov eax, 45h
	mov ebx, 12h
	mov eax, (eax XOR ebx)
invoke ExitProcess,0
main endp
end main
