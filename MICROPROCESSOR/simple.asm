section .data
msg db 10,"hi my name is xyz",10
msglen equ $-msg

msg1 db 9,"i study at mescoe",10
msglen1 equ $-msg1

%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

%macro print 4
mov rax,%1
mov rdi,%2
mov rsi,%3
mov rdx,%4
syscall
%endmacro

section .bss

section .txt
global_start:
_start:

print msg,msglen
print msg1,msglen1

print 1,1,msg,msglen
print 1,1,msg1,msglen1

mov rax,60
syscall

