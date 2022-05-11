.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
i WORD 1
a WORD 0
.code
main PROC
mov eax, 0
mov ecx, 10
L1:
	cmp i, cx
	jg next
	add ax, 5
	add i, 1
	jmp L1
next:
	mov a, ax
invoke ExitProcess,0
main endp
end main
