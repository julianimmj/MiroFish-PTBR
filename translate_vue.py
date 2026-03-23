import os

TRANSLATIONS = {
    "本体生成": "Gerar Ontologia",
    "生成中": "Gerando...",
    "LLMAnálise文档内容与Requisito de Simulação，提取出现实种子，自动生成合适的本体结构": "IA analisa o documento e os requisitos para extrair sementes do mundo e gerar automaticamente a estrutura da ontologia",
    "Uploading and analyzing docs...": "Enviando e analisando documentos...",
    "正在Análise文档...": "Analisando documentos...",
    "正在EnviarArquivo并Análise文档...": "Enviando arquivo e analisando documentos...",
    "Construção GraphRAG": "Construção GraphRAG",
    "等待": "Aguardando",
    "基于生成的本体，将文档自动分块后调用 Zep 构建知识Grafo，提取实体和Relações，并形成时序记忆与社区Resumo": "Com base na ontologia, os documentos são divididos no Zep para construir o Grafo de Conhecimento, extraindo entidades e relações.",
    "实体Nós": "Nós de Entidade",
    "Relações边": "Arestas de Relação",
    "SCHEMATipo": "Tipo de SCHEMA",
    "构建完成": "Construção Concluída",
    "Construção do GrafoConcluído，请进入Próxima Etapa进行模拟Configuração do Ambiente": "Grafo concluído. Vá para a Próxima Etapa (Configuração do Ambiente)",
    "Конструção do Grafo完成": "Construção do Grafo concluída",
    "Construção do Grafo中": "Construindo Grafo...",
    "等待本体生成": "Aguardando geração da ontologia",
    "Geração concluída后将自动开始构建Grafo": "A construção começará automaticamente após a geração",
    "Grafo数据Carregando...": "Carregando dados do Grafo...",
    "进入Configuração do Ambiente ➝": "Configurar Ambiente ➝",
    "进入Configuração do Ambiente": "Configurar Ambiente",
    "准备进入Próxima Etapa骤": "Preparando próxima etapa",
    "创建中...": "Criando...",
    "Projeto信息": "Informações do Projeto",
    "ProjetoNome": "Nome do Projeto",
    "ProjetoID": "ID do Projeto",
    "GrafoID": "ID do Grafo",
    "没有待Enviar的Arquivo，请Voltar ao Início重新Ações": "Sem arquivos, volte ao início para tentar novamente",
    "接口说明": "Descrição",
    "Enviar文档后，LLMAnálise文档内容，自动生成适合舆论模拟的本体结构（实体Tipo + RelaçõesTipo）": "Geração automática da estrutura da ontologia (Tipos de Entidade + Tipos de Relação)",
    "生成进度": "Progresso da Geração",
    "生成的实体Tipo": "Tipos de Entidade Gerados",
    "生成的RelaçõesTipo": "Tipos de Relação Gerados",
    "等待本体生成...": "Aguardando...",
    "基于生成的本体，将文档分块后调用 Zep API 构建知识Grafo，提取实体和Relações": "A API do Zep é chamada para construir o Grafo (entidades e relações)",
    "等待本体Geração concluída...": "Aguardando conclusão...",
    "Progresso da construção": "Progresso da Construção",
    "构建结果": "Resultados",
    "实体Tipo": "Tipos de Entidade",
    "实时知识Grafo": "Grafo Em Tempo Real",
    "实时更新中...": "Atualizando em tempo real...",
    "更多Relações...": "mais relações...",
    "数据即将显示...": "Os dados aparecerão em breve...",
    "退出Tela Cheia": "Sair da Tela Cheia",
    "Tela Cheia显示": "Tela Cheia",
    "AtualizarGrafo": "Atualizar Grafo",
    "初始化中": "Inicializando...",
    "构建失败": "Falha na Construção"
}

def translate_vue(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    count = 0
    for zh, pt in TRANSLATIONS.items():
        if zh in content:
            content = content.replace(zh, pt)
            count += 1
            
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{count} replaced] {os.path.basename(filepath)}")

def main():
    base = os.path.dirname(__file__)
    components = os.path.join(base, 'frontend', 'src', 'components')
    views = os.path.join(base, 'frontend', 'src', 'views')
    
    for d in [components, views]:
        for f in os.listdir(d):
            if f.endswith('.vue'):
                translate_vue(os.path.join(d, f))

if __name__ == '__main__':
    main()
