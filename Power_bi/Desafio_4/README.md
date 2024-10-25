# Desafio Prático: Criando um Star Schema para cenários de vendas com Power bi 
**Objetivo:** Criação de um esquema estrela com base no modelo que a professora disponibilizou, este esquema foi criado no MySQL.

**Observações:** 
- Foco no professor: quais são os professores?
- Departamentos : Quais são os departamentos ?
- Cursos que cada um ministra ?
- Tabela fato consiste no objetivo da análise , no caso aqui o professor.

 Foram eliminadas as tabelas não relacionadas , deixando apenas a tabela fato e as dimensões:
 
 **Tabela fato**
 
- Professor: São armazenadas informações sobre o professor , nome, sobrenome , idade , cpf , se está ativo ou não.
 
 **Tabelas Dimensões**
  
- Departamentos:Mantém informações sobre o departamento , nome_departamento e nome_campus.
- Curso: Mantém informações sobre o curso , nome_curso e area_estudo.
- Disciplina : Mantém informações sobre a disciplina , nome_disciplina e pre_requisito.

  Após a criação do esquema estrela , foram feitos os devidos relacionamentos , onde utilizamos o de muitos para um (N:1) entre as tabelas fato e dimensões.  



 
    
