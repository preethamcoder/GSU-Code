;Name Preetham Thelluri
;Class: CSC3210
;Assignment#: 3
;Description: This program attempts to cur a variable into words and find the sum of the parts.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword
.data
qVal QWORD 0506030704080102h
.code
main proc
mov edi, OFFSET qVal 
mov dx, WORD PTR [edi]
mov cx, WORD PTR [edi+2]
mov bx, WORD PTR [edi+4]
mov ax, WORD PTR [edi+6]
add ax, bx
add ax, cx
add ax, dx
invoke ExitProcess,0
main endp
end main
