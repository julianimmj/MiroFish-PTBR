import os

# Dicionário de traduções comuns da API para Português
TRANSLATIONS = {
    # Erros comuns
    "项目不存在": "Projeto não encontrado",
    "项目不存在或删除失败": "Projeto não encontrado ou falha ao excluir",
    "配置错误": "Erro de configuração",
    "ZEP_API_KEY未配置": "ZEP_API_KEY não configurada",
    "未知": "Desconhecido",
    "成功": "Sucesso",
    "失败": "Falha",

    # Graph API
    "项目已删除": "Projeto excluído",
    "项目已重置": "Projeto redefinido",
    "请提供模拟需求描述": "Forneça a descrição da necessidade da simulação",
    "请至少上传一个文档文件": "Envie pelo menos um arquivo de documento",
    "没有成功处理任何文档，请检查文件格式": "Nenhum documento processado com sucesso, verifique o formato",
    "请提供 project_id": "Forneça o project_id",
    "项目尚未生成本体，请先调用 /ontology/generate": "Ontologia não gerada, chame /ontology/generate primeiro",
    "图谱正在构建中，请勿重复提交。如需强制重建，请添加 force: true": "Grafo em construção, não envie novamente. Use force: true para forçar",
    "未找到提取的文本内容": "Conteúdo de texto não encontrado",
    "未找到本体定义": "Ontologia não encontrada",
    "图谱构建任务已启动": "Tarefa de construção do grafo iniciada",
    "图谱构建任务已启动，请通过 /task/{task_id} 查询进度": "Construção do grafo iniciada. Verifique /task/{task_id}",
    "任务不存在": "Tarefa não encontrada",
    "图谱已删除": "Grafo excluído",
    "创建Zep图谱...": "Criando Grafo Zep...",
    "设置本体定义...": "Definindo Ontologia...",
    "等待Zep处理数据...": "Aguardando processamento do Zep...",
    "获取图谱数据...": "Obtendo dados do grafo...",
    "图谱构建完成": "Construção do grafo concluída",
    "构建失败": "Falha na construção",
    "文本分块中...": "Dividindo texto em blocos...",

    # Simulation API
    "项目尚未完成图谱构建": "Construção do grafo do projeto não concluída",
    "模拟配置任务已启动": "Tarefa de configuração da simulação iniciada",
    "缺少必要参数": "Parâmetros obrigatórios ausentes",
    "项目尚未完成模拟配置": "Configuração da simulação do projeto não concluída",
    "模拟正在运行中，请勿重复启动": "A simulação já está em execução, não inicie novamente",
    "模拟运行任务已启动": "Tarefa de execução da simulação iniciada",
    "模拟未运行": "A simulação não está em execução",
    "模拟已停止": "Simulação parada",
    "没有模拟日志记录": "Nenhum log de simulação registrado",
    
    # Task messages
    "分析模拟需求...": "Analisando requisitos de simulação...",
    "生成实体配置文件...": "Gerando arquivo de configuração de entidades...",
    "生成环境配置文件...": "Gerando arquivo de configuração do ambiente...",
    "初始化模拟引擎...": "Inicializando motor de simulação...",
    "配置生成完成": "Configuração gerada com sucesso",
    "开始执行模拟...": "Iniciando execução da simulação...",
    "等待模拟完成...": "Aguardando conclusão da simulação...",
    "模拟执行完成": "Execução da simulação concluída",
    
    # Report API
    "报告生成任务已启动": "Tarefa de geração de relatório iniciada",
    "项目尚未完成模拟，无法生成报告": "Simulação não concluída, impossível gerar relatório",
    "请提供问题内容": "Forneça o conteúdo da pergunta",
    "未找到生成的报告": "Relatório gerado não encontrado",
    "回答生成完成": "Geração da resposta concluída",
    "生成报告中...": "Gerando relatório...",
    "分析模拟数据...": "Analisando dados da simulação...",
    
    # Interaction / UI
    "分析中...": "Analisando...",
    "处理中...": "Processando...",
    "完成": "Concluído"
}

def fast_translate(filepath):
    """Fast find and replace based on predefined dictionary."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
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
    base_dir = os.path.dirname(__file__)
    targets = [
        os.path.join(base_dir, 'backend', 'app', 'api'),
        os.path.join(base_dir, 'backend', 'app', 'services')
    ]
    
    for target in targets:
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith('.py'):
                    fast_translate(os.path.join(root, file))

if __name__ == '__main__':
    main()
