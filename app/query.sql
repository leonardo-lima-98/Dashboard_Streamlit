SELECT top 10000
    A.Id,
    CONCAT('https://apiprod.gpsvista.com.br/api/relatorio/tarefa?tarefaId=', A.Id) AS 'PDF',
	CASE
        WHEN A.Termino > A.TerminoReal THEN 'ATRASADO'
        ELSE 'NO PRAZO'
    END AS 'Verificação',
    A.Nome AS 'Nome_Tarefa',
    A.Inicio AS 'Programado_Inicio',
    A.InicioReal AS 'Real_Inicio',
    A.Termino AS 'Programado_Fim',
    A.TerminoReal AS 'Real_Fim',
    E.Nome AS 'Usuario',
    G.Descricao AS 'Pergunta',
    D.Conteudo AS 'Resposta',
    F.Descricao AS 'Local',
    A.EstruturaQRCode,
    A.EstruturaDescricao
    
FROM Tarefa A WITH (NOLOCK)

LEFT JOIN Execucao D WITH (NOLOCK) on D.TarefaId = A.Id
LEFT JOIN Pergunta G WITH (NOLOCK) on G.Id = D.PerguntaId
LEFT JOIN Recurso E WITH (NOLOCK) on E.CodigoHash = A.FinalizadoPorHash
LEFT JOIN DW_Vista.dbo.DM_ESTRUTURA F WITH (NOLOCK) on F.Id_Estrutura = A.EstruturaId

WHERE D.Conteudo is not null AND A.ChecklistId = '3b02cb03-231f-4e47-8583-be60203e391b'