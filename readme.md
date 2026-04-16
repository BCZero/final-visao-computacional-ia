🛡️ Detecção de Armas de Fogo (Pistolas e Fuzis) com YOLOv8Este projeto consiste no desenvolvimento e treinamento de um modelo de Visão Computacional para a detecção automatizada de armamentos em imagens. O projeto foi desenvolvido como trabalho prático final da disciplina de Visão Computacional e IA Generativa do MBA em Inteligência Artificial e Machine Learning.A solução foca na triagem automatizada de ameaças, visando otimizar processos de segurança pública e análise de evidências em contextos investigativos.

🚀 Tecnologias Utilizadas
- Python 3.12YOLOv8 (Ultralytics): Arquitetura de detecção de objetos.
- OpenCV: Processamento de imagens.
- PyTorch: Framework de Deep Learning.
- UV: Gerenciador de pacotes e ambientes Python de alta performance.

📊 Resultados e Métricas

Métrica,Resultado
mAP@0.50 (Geral),87.4%
Precisão Média,92.3%
Recall Médio,64.7%
Pistola (AP@50),89.1%
Fuzil (AP@50),85.7%

Nota Técnica: A alta precisão (92.3%) garante baixíssima taxa de alarmes falsos, tornando o modelo confiável para alertas operacionais.

🛠️ Instalação e ConfiguraçãoPara reproduzir os resultados, certifique-se de ter o uv instalado.Clonar o repositório:

Bash
git clone https://github.com/BCZero/final-visao-computacional-ia.git

cd trabalho-visao-computacional

Criar e ativar o ambiente virtual:

Bash
uv venv venv_trabalho --python 3.11.9

# No Windows:

.\venv_trabalho\Scripts\Activate.ps1

Instalar dependências:
Bash
uv pip install -r requirements.txt

🔍 Como Executar a InferênciaPara testar o modelo em uma imagem nova, utilize o script inferencia.py passando o caminho dos pesos e da imagem desejada:
Bash
python inferencia.py best.pt sample_images/sua_imagem.jpg

Os resultados (imagens com as bounding boxes) serão salvos automaticamente na pasta runs/detect/predict.

📂 Estrutura do Projeto

├── dataset/             # Estrutura de pastas train/val/test
├── sample_images/       # Imagens de exemplo para teste rápido
├── best.pt              # Pesos treinados do modelo (YOLOv8)
├── config.yaml          # Configurações de classes e caminhos do dataset
├── inferencia.py        # Script para execução de predições
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação

✒️ AutorBruno Sampaio
Estudante de Análise e Desenvolvimento de Sistemas
Especialista em formação em IA e Machine Learning
