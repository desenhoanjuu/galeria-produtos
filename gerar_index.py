
import os

PASTA_IMAGENS = "produtos"
ARQUIVO_HTML = "index.html"

template_inicio = """<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Galeria de Produtos</title>
  <style>
    body { font-family: sans-serif; background: #f9f9f9; margin: 0; padding: 2rem; }
    h1 { text-align: center; margin-bottom: 1rem; }
    .busca { text-align: center; margin-bottom: 2rem; }
    .busca input { padding: 0.5rem; width: 250px; font-size: 1rem; }
    .galeria { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; }
    .produto { background: white; padding: 1rem; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); text-align: center; }
    .produto img { max-width: 100%; height: auto; border-radius: 8px; }
    .produto .nome { margin-top: 1rem; font-weight: bold; }
    .produto .codigo { color: #888; font-size: 0.9rem; }
    .lista-codigos { margin-top: 3rem; font-size: 0.9rem; color: #555; text-align: center; }
  </style>
</head>
<body>
  <h1>Galeria de Produtos</h1>
  <div class="busca">
    <input type="text" id="campoBusca" placeholder="Buscar por código ou nome..." onkeyup="buscarProduto()">
  </div>
  <div class="galeria" id="galeria">
"""

template_fim = """  </div>
  <div class="lista-codigos">
    <h2>Códigos cadastrados</h2>
    <div id="listaCodigos"></div>
  </div>
  <script>
    const produtos = document.querySelectorAll('.produto');
    const codigos = new Set();
    produtos.forEach(p => codigos.add(p.dataset.codigo));
    document.getElementById('listaCodigos').innerText = Array.from(codigos).sort().join(', ');

    function buscarProduto() {
      const termo = document.getElementById('campoBusca').value.toLowerCase();
      produtos.forEach(p => {
        const nome = p.dataset.nome;
        const codigo = p.dataset.codigo;
        p.style.display = nome.includes(termo) || codigo.includes(termo) ? 'block' : 'none';
      });
    }
  </script>
</body>
</html>
"""

def gerar_index():
    imagens = [f for f in os.listdir(PASTA_IMAGENS) if f.endswith(".jpg")]
    with open(ARQUIVO_HTML, "w", encoding="utf-8") as f:
        f.write(template_inicio)
        for img in imagens:
            nome = img.replace(".jpg", "")
            partes = nome.split("_")
            codigo = partes[-1]
            nome_formatado = " ".join(partes[:-1]).capitalize()
            f.write(f'''    <div class="produto" data-nome="{nome_formatado.lower()}" data-codigo="{codigo}">
      <img src="{PASTA_IMAGENS}/{img}" alt="{nome_formatado}">
      <div class="nome">{nome_formatado}</div>
      <div class="codigo">{codigo}</div>
    </div>
''')
        f.write(template_fim)
    print(f"✅ index.html gerado com {len(imagens)} imagens.")

if __name__ == "__main__":
    gerar_index()
