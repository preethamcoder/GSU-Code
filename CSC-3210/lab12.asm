.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
array1 BYTE 13h, 14h, 15h, 16h
array2 BYTE 12h, 13h, 14h, 15h
maxlength BYTE ($-array2)/(TYPE array2) ;It doesn't matter here because both arrays are of same length
sample1 BYTE 030h
sample2 BYTE 05h
index BYTE 0
exp1 WORD 0
.code
main PROC
movzx eax, index
mov ecx, 0
mov esi, OFFSET array1
mov edx, OFFSET array2
mov ebx, 0
beginwhile:
	cmp cl, maxlength
	jge L1
	mov al, [esi]
	cmp al, [edx]
	je L2
	jle L2
	mul sample1
	mov bx, ax
	mov eax, 0
	mov al, [edx]
	imul sample2
	xchg ax, bx
	cmp bl, 0
	je L2
	div bl
	inc esi
	inc edx
	inc ecx
	jmp beginwhile
L2:
	mov ax, 0
	inc esi
	inc edx
	inc edx
	jmp beginwhile
L1:
	movzx cx, al
	mov exp1, cx
invoke ExitProcess,0
main endp
end main
