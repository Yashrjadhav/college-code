section .data
msg db 10,"program to display positive and negative numbers",10
msglen equ $-msg

msg2 db 9," positive numbers are:",10
msglen2 equ $-msg2

msg3 db 9,"negative numbers are :",10
msglen3 equ $-msg3

%macro print 2
mov rax,1
mov rdi,1
mov rsi,%1
mov rdx,%2
syscall
%endmacro

array db 12h,90h,87h,88h,7ah,0ah,02h
pcnt db 0
ncnt db 0
newline db 10
section .bss
dispbuff resb 2
section .txt

global_start:
_start:

print msg,msglen
mov rsi,array
mov rcx,07

again:
bt qword[rsi],07
jnc pnxt
inc byte[ncnt]
jmp pskip
pnxt:inc byte [pcnt]
pskip:inc rsi,1
loop again

print msg1,msglen1
mov bl,[pcnt]
call disp_result
print newline,1
print msg2,msglen2
mov bl,[ncnt]
call disp_result
print newline,1

mov rax,60
mov rdi,0
syscall

disp_result:
mov rdi,dispbuff
mov rcx,02
dispup1;
rol bl,4
mov dl,bl
and dl,,0fh
add dl,39h
jbe dispskip1
add dl,07h

dispskip1:
mov[rdi],dl
inc rdi
loop dispup1
print dispbuff,2
ret

