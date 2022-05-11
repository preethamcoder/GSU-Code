.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: dword
.data 
Sum DWORD 0
n DWORD 4
.code
main PROC
	mov edx, n
	mov eax, 0
	mov ecx, 1
	call AddEm
INVOKE ExitProcess, 0
main ENDP
AddEm PROC
	cmp edx, ecx
	jb exit
	add eax, ecx
	inc ecx
	call AddEm
	exit:
		mov Sum, eax
		ret
AddEm ENDP
End main
