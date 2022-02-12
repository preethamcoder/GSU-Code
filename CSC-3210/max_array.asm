.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
Array WORD 10, 2, 23, 45, 21, 11
MAXIMUM WORD ?
.code
main PROC
mov ecx, 5
mov esi, OFFSET Array
mov edx, OFFSET MAXIMUM
mov ax, [esi]
mov [edx], ax
cmp [edx], ax
jge L1
L1:
	add esi, 2
	mov ax, [esi]	
	cmp ax, [edx]
	jle L2
	mov [edx], ax
	;LOOP L1
L2:
	;mov [edx], ax
	LOOP L1
invoke ExitProcess,0
main endp
end main
