from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sql
from datetime import *

def limpar():
    for widgets in frame.winfo_children():
        widgets.destroy()
    
def bt_ent():
    global usu, serie
    usu = usuInp.get()
    serie = seriInp.get()

    consu()
    if ler == []:
        messagebox.showwarning(title='Loguin', message='Usuário inexistente')
    else:    
        for l in ler:
            if l[0] == usu and l[1] == serie:
                limpar()
                tela2()

def bt_back():
    jnl.config(menu=barraMenu)
    limpar()
    tela()

def bt_backTl2():
    limpar()
    tela2()

def cnt():
    global conexao
    conexao = sql.connect(
        host= 'localhost',
        user= 'root',
        password= '1234',
        database= 'biblioteca'
    )
    print('conexao estabelecida')

def consuCod():
    global lerCod
    cnt()
    cod = codInp.get()
    cursor = conexao.cursor()
    cmd = f'SELECT id FROM livros WHERE cod_livro = {cod}'
    cursor.execute(cmd)
    lerCod = cursor.fetchall()
    print(lerCod)

    cursor.close()
    conexao.close()

def bt_save():
    global msg, liv, cod, data
    consuCod()
    cod = codInp.get()
    data = date.today()
    print(data)

    if lerCod == []:
        messagebox.showwarning(title='Erro', message='Codigo do livro inexistente!')
    else:
        cnt()
        cursor = conexao.cursor()
        cmd = f'SELECT id FROM alunos WHERE  nome_aluno = "{usu}"'
        cursor.execute(cmd)
        idUsu = cursor.fetchone()
        cmd2 = f'SELECT id FROM livros WHERE cod_livro = {cod}'
        cursor.execute(cmd2)
        codLiv = cursor.fetchone()
        cmd3 = f'INSERT INTO emprestimo (data_emp, confirm ,alunos_id, livros_id, usuario_id) VALUES ("{data}", 0 , {int(idUsu[0])}, {int(codLiv[0])}, 1)'
        cursor.execute(cmd3)
        conexao.commit()
        print(int(idUsu[0]))
        print(int(codLiv[0]))
        cursor.close()
        conexao.close()
        data += timedelta(7)
        dtEnt.set(data)
        messagebox.showinfo(title='Informações', message=f'Salvo com sucesso!')
        
def buscar():
    global buscNome
    usuNome = usuInp.get()
    nomes = []
    print(usuNome)
    cnt()
    cursor = conexao.cursor()
    cmd = f'SELECT nome_aluno FROM alunos WHERE nome_aluno LIKE "{usuNome}%"' 
    cursor.execute(cmd)
    buscNome = cursor.fetchall()
    print(buscNome)

    for l in buscNome:
        nomes.append(str(l[0]))
    print(nomes)
    usuInp['values'] = nomes

    cursor.close()
    conexao.close()
  
def consu():
    global ler
    cnt()
    usu = usuInp.get()
    serie = seriInp.get()

    cursor = conexao.cursor()
    cmd = f'SELECT nome_aluno, serie FROM alunos WHERE nome_aluno = "{usu}" AND serie = "{serie}"'
    cursor.execute(cmd)
    ler = cursor.fetchall()
    print(ler)

    cursor.close()
    conexao.close()

def prenDadosPend(event):
    cnt()
    nome_liv = inpPend.get()
    nome_alu = aluPend.get()
    dtList = []
    cursor = conexao.cursor()
    cmd = f'SELECT id FROM livros WHERE nome_livro = "{nome_liv}"'
    cursor.execute(cmd)
    lerId = cursor.fetchall()
    print(lerId)
    for l in lerId:
        dtList.append(int(l[0]))
    print(dtList)
    cmd2 = f'select data_emp from alunos a join emprestimo e on a.id = e.alunos_id join livros l on l.id = e.livros_id where alunos_id={nome_alu} AND livros_id= "{dtList[0]}"'
    cursor.execute(cmd2)
    lerDataPend = cursor.fetchall()
    print(lerDataPend)
    dtEmpPend.set(lerDataPend[0])
    inpDtPend['values'] = lerDataPend

    cursor.close()
    conexao.close()

def consuPend():
    nome_alu = aluPend.get()
    livros = []
    cnt()
    cursor = conexao.cursor()
    cmd = f'SELECT a.nome_aluno, l.nome_livro FROM alunos a JOIN emprestimo e ON a.id = e.alunos_id JOIN livros l ON l.id = e.livros_id WHERE e.alunos_id = "{nome_alu}" AND confirm = 0'
    cursor.execute(cmd)
    lerPend = cursor.fetchall()

    for l in lerPend:
        livros.append(str(l[1]))
    inpPend['values'] = livros

    cursor.close()
    conexao.close()

def confDevol():
    
    nomLiv = inpPend.get()
    dt = inpDtPend.get()
    if nomLiv == '':
        messagebox.showwarning(title='Devolução', message='Selecione um livro')
    else:
        cnt()
        cursor = conexao.cursor()
        cmd = f'SELECT id FROM livros WHERE nome_livro = "{nomLiv}"'
        cursor.execute(cmd)
        idLiv = cursor.fetchone()
        print(idLiv)
        cmd2 = f'UPDATE emprestimo SET confirm = 1 WHERE confirm = 0 AND livros_id = {idLiv[0]} AND data_emp = "{dt}"'
        cursor.execute(cmd2)
        conexao.commit()

        cursor.close()
        conexao.close()
        messagebox.showinfo(title='Devolução', message='Devolução feita com sucesso!')
        tlConfDevol()
    
def tlConfDevol():
    global aluPend, inpPend, dtEmpPend, inpDtPend ,IDUSu
    limpar()
    dtEmpPend = StringVar()
    IDUsu = StringVar()
    jnl.title('Devolução')
    barraMenu2 = Menu(frame)
    barraMenu2.add_command(label='Home', font=('Arial', 8), command=tela)
    menuConsu = Menu(barraMenu2, tearoff=0)
    menuConsu.add_command(label='Devolução', font=('Arial', 8), command=tlConfDevol)
    menuConsu.add_command(label='Pendentes', font=('Arial', 8), command=tlPend)
    barraMenu2.add_cascade(label='Consulta', menu=menuConsu)
    jnl.config(menu=barraMenu2)

    aluPend = Entry(frame, font=('Arial', 9), textvariable=IDUsu)
    aluPend.place(x=100, y=10, width=100, height=20)

    busca = PhotoImage(file='images\pesquisa.png')
    busca = busca.subsample(40,40)
    figura = Label(frame, image=busca)
    figura.image = busca

    btPend = Button(frame, text='Buscar', font=('Arial', 9), command=consuPend, image= busca)
    btPend.place(x=210, y=10, width=20, height=20)

    inpPend = ttk.Combobox(frame, font=('Arial', 9), state='readonly')
    inpPend.place(x=10, y=50, width=200, height=20)

    inpDtPend = ttk.Combobox(frame, textvariable=dtEmpPend, state='readonly', font=('Arial', 9))
    inpDtPend.place(x=230, y=50, width=100, height=20)

    btSalv = Button(frame, text= 'Salvar', font=('Arial', 9), command=confDevol)
    btSalv.place(x=20, y=115, width=70, height=20)
    btVolt = Button(frame, text='Voltar', font=('Arial', 9), command=bt_backTl2)
    btVolt.place(x=110, y=115, width=70, height=20)

    cnt()
    cursor = conexao.cursor()
    cmd = f'SELECT id FROM alunos WHERE  nome_aluno = "{usu}"'
    cursor.execute(cmd)
    idUsu = cursor.fetchone()
    IDUsu.set(idUsu)

    inpPend.bind('<<ComboboxSelected>>', prenDadosPend)

def tlPend():
    global aluPend, inpPend, dtEmpPend, inpDtPend ,IDUSu
    limpar()
    dtEmpPend = StringVar()
    IDUsu = StringVar()
    jnl.title('Pendentes')
    barraMenu2 = Menu(frame)
    barraMenu2.add_command(label='Home', font=('Arial', 8), command=tela)
    menuConsu = Menu(barraMenu2, tearoff=0)
    menuConsu.add_command(label='Devolução', font=('Arial', 8), command=tlConfDevol)
    menuConsu.add_command(label='Pendentes', font=('Arial', 8), command=tlPend)
    barraMenu2.add_cascade(label='Consulta', menu=menuConsu)
    jnl.config(menu=barraMenu2)

    aluPend = Entry(frame, font=('Arial', 9), textvariable=IDUsu)
    aluPend.place(x=100, y=10, width=100, height=20)

    busca = PhotoImage(file='images\pesquisa.png')
    busca = busca.subsample(40,40)
    figura = Label(frame, image=busca)
    figura.image = busca

    btPend = Button(frame, text='Buscar', font=('Arial', 9), command=consuPend, image=busca)
    btPend.place(x=210, y=10, width=20, height=20)

    inpPend = ttk.Combobox(frame, font=('Arial', 9), state='readonly')
    inpPend.place(x=10, y=50, width=200, height=20)

    inpDtPend = ttk.Combobox(frame, textvariable=dtEmpPend, state='readonly', font=('Arial', 9))
    inpDtPend.place(x=230, y=50, width=100, height=20)

    btVolt = Button(frame, text='Voltar', font=('Arial', 9), command=bt_backTl2)
    btVolt.place(x=20, y=115, width=70, height=20)

    cnt()
    cursor = conexao.cursor()
    cmd = f'SELECT id FROM alunos WHERE  nome_aluno = "{usu}"'
    cursor.execute(cmd)
    idUsu = cursor.fetchone()
    IDUsu.set(idUsu)
    
    inpPend.bind('<<ComboboxSelected>>', prenDadosPend)

def saveCad():
    valCad = inpCad.get()
    seriCad = inpCadSeri.get()
    
    if valCad == '':
        messagebox.showwarning(title='Cadastro', message='Por favor preencher os campos!')
    else:        
        cnt()
        cursor = conexao.cursor()
        cmd = f'INSERT INTO alunos (nome_aluno, serie) VALUES ("{valCad}", "{seriCad}")'
        cursor.execute(cmd)
        conexao.commit()
        cursor.close()
        conexao.close()
        inpCad.delete(0, END)
        messagebox.showinfo(title='Cadastro', message='Usuário cadastrado com sucesso!')

def jnlCadastro():
    global inpCad, inpCadSeri, jnlCad
    limpar()
    jnl.title('Cadastro Usuário')

    usuCad = Label(frame, text='Usuário', font=('Arial', 9))
    usuCad.place(x=20, y=30, width=50, height=20)
    inpCad = Entry(frame, font=('Arial', 9))
    inpCad.place(x=80, y=30, width=200, height=20)

    seriCadastro = Label(frame, text='Série', font=('Arial', 9))
    seriCadastro.place(x=10, y=70, width=50, height=20)
    inpCadSeri = ttk.Combobox(frame, values=series, font=('Arial', 9), state='readonly')
    inpCadSeri.set('8º')
    inpCadSeri.place(x=80, y=70, width=50, height=20)

    btSaveCad = Button(frame, text='Salvar', font=('Arial', 9), command=saveCad)
    btSaveCad.place(x=20, y=115, width=70, height=20)

    btVoltCad = Button(frame, text='Voltar', font=('Arial', 9), command=bt_back)
    btVoltCad.place(x=110, y=115, width=70, height=20)

def saveLiv():
    inpLiv = inpLivCad.get()
    inpCod = inpCodCad.get()

    if inpLiv == '' and inpCod == '':
        messagebox.showwarning(title='Cadastro Livro', message='Por favor preencher os campos!')
    elif inpLiv == '':
        messagebox.showwarning(title='Cadastro Livro', message='Por favor preencher os campos!')
    elif inpCod == '':
        messagebox.showwarning(title='Cadastro Livro', message='Por favor preencher os campos!')
    else:
        cnt()
        cursor = conexao.cursor()
        cmd = f'INSERT INTO livros (nome_livro, cod_livro) VALUES ("{inpLiv}", {inpCod})'
        cursor.execute(cmd)
        conexao.commit()
        
        cursor.close()
        conexao.close()

        inpLivCad.delete(0,END)
        inpCodCad.delete(0,END)
        messagebox.showinfo(title='Cadastro Livro', message='Livro cadastrado com sucesso!')

def jnlCadLiv():
    global inpLivCad, inpCodCad, jnlLiv
    
    limpar()
    jnl.title('Cadastro Livro')


    cadCod = Label(frame, text= 'Código', font=('Arial', 9))
    cadCod.place(x=20, y=30, width=50, height=20)
    inpCodCad = Entry(frame, font=('Arial', 9))
    inpCodCad.place(x=80, y=30, width=200, height=20)

    cadLiv = Label(frame, text= 'Livro', font=('Arial', 9))
    cadLiv.place(x=10, y=70, width=50, height=20)
    inpLivCad = Entry(frame, font=('Arial', 9))
    inpLivCad.place(x=80, y=70, width=200, height=20)

    btSaveLiv = Button(frame, text='Salvar', font=('Arial', 9), command=saveLiv)
    btSaveLiv.place(x=20, y=115, width=70, height=20)
    btVoltLiv = Button(frame, text='Voltar', font=('Arial', 9), command=bt_back)
    btVoltLiv.place(x=110, y=115, width=70, height=20)

def tela2():
    global jnl2, codInp, livInp, dtEnt, barraMenu2
    

    dtEnt = StringVar()
    codTxt = Label(frame, text= 'Código', font=('Arial', 9))
    codTxt.place(x=20, y=30, width=50, height=20)
    codInp = Entry(frame, font=('Arial', 9))
    codInp.place(x=80, y=30, width=200, height=20)

    data = Label(frame, text='Entregar', font=('Arial', 9))
    data.place(x=20, y=70, width=50, height=20)
    dataInp = Entry(frame, font=('Arial', 9), state='readonly', textvariable=dtEnt)
    dataInp.place(x=80, y=70, width=200, height=20)

    bt_salv = Button(frame, text= 'Salvar', font=('Arial', 9), command=bt_save)
    bt_salv.place(x=20, y=115, width=70, height=20)

    bt_volt = Button(frame, text= 'Voltar', font=('Arial', 9), command=bt_back)
    bt_volt.place(x=110, y=115, width=70, height=20)

    barraMenu2 = Menu(frame)
    barraMenu2.add_command(label='Home', font=('Arial', 8), command=tela)
    menuConsu = Menu(barraMenu2, tearoff=0)
    menuConsu.add_command(label='Devolução', font=('Arial', 8), command=tlConfDevol)
    menuConsu.add_command(label='Pendentes', font=('Arial', 8), command=tlPend)
    barraMenu2.add_cascade(label='Consulta', menu=menuConsu)
    jnl.config(menu=barraMenu2)
    
def prenSeri(event):
    cnt()
    aluno = usuInp.get()
    cursor = conexao.cursor()
    cmd = f'SELECT serie FROM alunos WHERE nome_aluno = "{aluno}"'
    cursor.execute(cmd)
    ler = cursor.fetchall()
    seriPren.set(ler)

def tela():
    limpar()
    global usuInp, seriInp, bsc, bt_en, usuTxt, seriTxt, series, jnl, seriPren, barraMenu
    seriPren = StringVar()
    jnl.title('Loguin')
    jnl.geometry('350x170')

    usuTxt = Label(frame, text= 'Usuário', font=('Arial', 9) )
    usuTxt.place(x=20, y=30, width=50, height=20)
    usuInp = ttk.Combobox(frame, font=('Arial', 9))
    usuInp.place(x=80, y=30, width=200, height=20)
    
    busca = PhotoImage(file='images\pesquisa.png')
    busca = busca.subsample(40,40)
    figura = Label(frame, image=busca)
    figura.image = busca

    bsc = Button(frame, image=busca, font=('Arial', 9), command=buscar)
    bsc.place(x=290, y=30, width=20, height=20)
    
    seriTxt = Label(frame, text= 'Série', font=('Arial', 9))
    seriTxt.place(x=10, y=70, width=50, height=20)
    series = ['8º', '9A', '9B', '1A', '1B', '1C', '1D', '2A', '2B', '2C', '3A', '3B']
    seriInp = ttk.Combobox(frame, values= series, font=('Arial', 9), textvariable=seriPren, state='readonly')
    seriInp.set('8º')
    seriInp.place(x=80, y=70, width=50, height=20)
    bt_en = Button(frame, text='Entrar', font=('Arial', 9), command=bt_ent)
    bt_en.place(x=20, y=115, width=70, height=20)

    barraMenu = Menu(jnl)
    menuCadastro = Menu(barraMenu, tearoff=0)
    menuCadastro.add_command(label='Alunos', font=('Arial', 8), command=jnlCadastro)
    menuCadastro.add_command(label='Livros',font=('Arial', 8), command=jnlCadLiv)
    barraMenu.add_cascade(label='Cadastro', menu=menuCadastro)
    jnl.config(menu=barraMenu)
    
    usuInp.bind('<<ComboboxSelected>>', prenSeri)

jnl = Tk()

frame = Frame(jnl)
frame.pack(expand=True, fill='both')
jnl.iconbitmap('images\icon.ico')
tela()

jnl.mainloop()