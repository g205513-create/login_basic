import customtkinter as ctk

ctk.set_appearance_mode('light')

app=ctk.CTk()
app.title('Sistema de login')
app.geometry('500x400')


#criação de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'g205513@gmail.com' and senha == 'gustavoGuanabara155':    
        label_feedback.configure(text='Login feito com sucesso!',
        text_color='green')     
    else:
        label_feedback.configure(text='Email ou senha incorretos!',
        text_color='red')



# campos
label_usuario = ctk.CTkLabel(app, text='Email:').pack(pady=0)

#entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digita o email:')
campo_usuario.pack(pady=10)

#Label
ctk.CTkLabel(app, text='Senha:').pack(pady=10)

#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digita a senha:')
campo_senha.pack(pady=10)

#button
botao_login=ctk.CTkButton(app, text='Entrar', command=validar_login)

botao_login.pack(pady=10)

#campo de feedback
label_feedback = ctk.CTkLabel(app,text='')
label_feedback.pack(pady=10)



app.mainloop()