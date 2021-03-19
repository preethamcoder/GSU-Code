.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
val1 BYTE 12
val2 BYTE 9
val3 BYTE 2
.code
main proc
	movzx ax, val2
	neg ax
	add ax, 7
	movzx bx, val3
	neg bx
	movzx cx, val1
	add bx, cx
	sub ax, bx
	mov bx, ax
invoke ExitProcess,0
main endp
end main
