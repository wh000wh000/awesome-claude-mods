<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods incríveis do Claude">
</p>

<h1 align="center">Mods incríveis do Claude</h1>

<p align="center"><b>O índice de mods e plugins do Claude Code classificados por evidências, além dos comportamentos mais profundos que eles alteram.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-595-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Português</b> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice ativo** · Última sincronização: `2026-10-12T03:53:55+08:00` (UTC+8)
> · Entradas: **595** · Adicionadas na atualização mais recente: **0** · Linguagens de implementação: **12**

<sub>Cada entrada abaixo foi coletada, filtrada e verificada novamente de forma automática. Nada aqui é uma inserção paga.</sub>

<a id="featured"></a>

## Destaques do momento

<sub>Uma entrada por categoria, classificada pelo grau de evidência e pelo número de estrelas, recalculada a cada atualização. É uma classificação, não uma recomendação; cada destaque leva ao respectivo card completo abaixo. Projetos que publicaram uma captura de tela ou uma gravação têm preferência, para que a faixa continue visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9478 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2535 · Python · 👁️ observed</sub>
<sub>Encontre os tokens fantasmas. Corrija-os. Sobreviva à compactação. Evite a degradação da qualidade do contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74351 · TypeScript · 👁️ observed</sub>
<sub>🌊 O agent harness original. Implante enxames inteligentes multiagente, coordene fluxos de trabalho autônomos e crie sistemas de IA conversacional. Inclui memória…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b>
<sub>⭐6 · 👁️ observed</sub>
</td>
</tr>
</table>

## Conteúdo

- [O que é um mod do Claude Code](#o-que-é-um-mod-do-claude-code)
- [Como as entradas são classificadas](#como-as-entradas-são-classificadas)
- [Oficial: repositórios próprios de Anthropic e notas de versão](#oficial-repositórios-próprios-de-anthropic-e-notas-de-versão) — **14**
- [Mods: criados com a capacidade de modificação](#mods-criados-com-a-capacidade-de-modificação) — **464**
- [Ecossistemas de plugins do DSH e do Cordis](#ecossistemas-de-plugins-do-dsh-e-do-cordis) — **106**
- [Textos, discussões e vídeos](#textos-discussões-e-vídeos) — **11**
- [Projetos por linguagem de implementação](#projetos-por-linguagem-de-implementação)

## O que é um mod do Claude Code

O Claude Code ganhou **mods** na versão 2.1.287: extensões que podem alterar comportamentos mais profundos do que um plugin conseguiria e desenhar sua própria interface.

Um mod pode usar hooks de `ui.render` para desenhar uma **linha, faixa, painel ou cartão** ao redor do prompt, ler o texto que você selecionou por último com `$.ui.selection()`, criar colegas de equipe com `agent.spawn` e controlar uma região de `Client`. Um mod que falha ao desenhar falha sozinho — `ui.fault` impede que um único mod defeituoso derrube a sessão.

Esta lista abrange mods, a superfície de plugins e hooks sobre a qual eles são construídos e os equivalentes no DSH e no Cordis. Deliberadamente, ela **não** abrange o ecossistema mais amplo do Claude Code: um pacote de prompts não é um mod.

## Como as entradas são classificadas

A maioria das listas desse espaço afirma o que está incluído. Esta informa quanto foi realmente verificado e permite filtrar de acordo. Uma classificação descreve as evidências, não a qualidade do projeto — um mod bem construído sobre o qual ninguém escreveu ainda continua sendo `inferred`.

| Classificação                                                                          | O que significa                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `publicado pelo próprio Anthropic`                                                     | Publicado pelo próprio Anthropic ou lido diretamente no changelog oficial.                                                                                                                                         |
| `o próprio texto menciona um mod API ou declara a capacidade de mods`                  | O próprio texto menciona parte da superfície de mods — `ui.render`, `ui.fault`, `agent.spawn`, `$.ui.selection()`, um painel, faixa ou cartão — então o autor está descrevendo algo desenvolvido sobre o API real. |
| `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` | Ele se descreve como um mod, plugin ou hook, mas nada em seu texto menciona especificamente a superfície de mods. É real, mas não confirmado.                                                                      |
| `correspondeu apenas pelo vocabulário`                                                 | Correspondeu apenas pelo vocabulário. Incluído para que o filtro seja auditável, não porque se acredite nele.                                                                                                      |

<a id="official"></a>

## Oficial: repositórios próprios de Anthropic e notas de versão

Repositórios de código do Anthropic Claude e os lançamentos que definiram a superfície de mods. Leia diretamente da fonte, em vez de um resumo.

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150197 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code é uma ferramenta de programação agêntica que funciona no seu terminal, entende sua base de código e ajuda você a programar mais rápido executando tarefas rotineiras, explicando códigos complexos e gerenciando fluxos de trabalho do git — tudo por meio de comandos em linguagem natural.

<sub>🔧 Encontrado em uso no código: `feed.xml`, `mods/diff/README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | TypeScript                                                      |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150197** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9478 · TypeScript · ✅ official · 2 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | TypeScript                                                      |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9478**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8249 · Python · ✅ official · 2 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | Python                                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8249**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6345 · Python · ✅ official · 242 天</summary>

##### 📝 Summary

Uma Action de revisão de segurança com IA GitHub usando Claude para analisar alterações de código em busca de vulnerabilidades de segurança.

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | Python                                                          |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6345**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1798 · Shell · ✅ official · 2 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | Shell                                                           |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1798**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 310 天</summary>

##### 📝 Summary

Materiais suplementares para Claude Model Cards

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2025-12-05 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.287 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Adicionados Mods do Claude: os plugins agora podem modificar comportamentos mais profundos. Adicionado You should know, um mod integrado no qual um agente auxiliar cuida de você e sinaliza coisas que você ou Claude podem não perceber. Ative-o com `/plugin enable cc-plugin-you-should-know@builtin` (para sessões first-party com telemetria ativada)

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.288 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Adicionado `$.ui.selection()` para mods: retorna o texto selecionado por último no modo de tela cheia e, quando a seleção está dentro de uma linha da transcrição, retorna essa linha. Corrigido um mod cujo botão às vezes executava a ação de outro botão quando pressionado em uma visualização desenhada antes de o código Claude ser reiniciado. Corrigidas sessões de tela cheia que saíam com "unrecoverable interface error" ao abrir a caixa de diálogo de tarefas em segundo plano enquanto um plugin ou mod mostrava linhas acima do prompt. Corrigido `claude plugin test` informando remotamente que os mods estavam desativados quando apenas havia lido uma configuração salva desatualizada

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.289 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Corrigido o problema em que uma regra de negar ou perguntar em uma parte aninhada de um comando shell composto não se mantinha após a aprovação de um mod instalado pelo usuário em máquinas gerenciadas. Corrigido o problema em que mods instalados não eram carregados na primeira sessão após uma atualização. Adicionado `agent.spawn` para colegas de equipe, um id de agente em todos os eventos de hooks de plugins e nos estados ocioso e de espera em `$.agent.list()`. Corrigidas sessões que terminavam com "unrecoverable interface error" quando um valor escrito pelo hook `ui.render` de um mod fazia uma linha falhar ao ser desenhada; o mecanismo agora desenha sua própria linha. Corrigido o conteúdo alinhado à direita no painel ou faixa de um mod sendo desenhado sob a marca de fechamento ou `\[-\]`, wh

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.290 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Adicionado `serverToolUses` ao resultado do hook `turn.step` de um mod: a ferramenta chama o API executado pelo próprio mod (o consultor), cada um com seu id, nome, entrada, início e fim. Adicionado `ceiling` à pergunta e ao veredito lidos pelo hook `tool.check` de um mod, nomeando a aprovação exigida por uma organização para uma ferramenta. Adicionados os tipos `ThemeKey` e `Color` às tipagens dos hooks de plugins, para que um editor liste as cores de tema que o desenho de um mod pode nomear. Adicionado a `claude plugin validate`: cada hook registrado por um mod em um ponto de controle é listado com a indicação de ter um `.catch` (`gatingHooks` em `--json`). Corrigido o resultado `turn.step` de um mod.

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.292 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Adicionado `prompt.autocomplete`, um evento ao qual um mod se conecta para adicionar suas próprias linhas à lista de preenchimento automático da caixa de prompt. Adicionado cache de prompt a `$.model.complete` para mods: `prompt` e `system` recebem blocos de texto, e `cache: true` em um bloco armazena a solicitação em cache até ele. Adicionados agentes de workflow ao hook de mod `agent.spawn`, com sua execução e índice, para que um mod possa recusá-los. Corrigidas linhas de Write, Edit, NotebookEdit e LSP, e linhas únicas de Read, Grep e Glob, ocultando por que um mod negou a chamada: a linha agora mostra o motivo. Corrigido um hook `config.set`, `state.set`, `env.set` ou `agent.spawn` de um mod que nega apó

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-07 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md">Claude Code 2.1.293 — the mod surface</a></b> · ✅ official</summary>

##### 📝 Summary

Adicionado `isDeferred` a `$.tool.register` para mods: `false` lista o esquema da ferramenta no prompt desde o início, em vez de mantê-lo atrás da busca de ferramentas Corrigidos os hooks de um mod em eventos `classic.*` que eram ignorados enquanto o worker de hooks do plugin reiniciava, deixando os hooks de configurações responderem sem eles Corrigida a falha de `claude plugin test` em mods que chamam `$.session.append`; os testes podem ler de volta as linhas anexadas com o novo `mock.session`

##### 📌 Basic facts

| Field    | Value                                                           |
| -------- | --------------------------------------------------------------- |
| Category | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence | `publicado pelo próprio Anthropic`                              |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 2</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Adicionado `$.ui.notify` aos mods: emite uma notificação nativa usando sua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corrigido o Esc ou uma interrupção durante um hook de `UserPromptSubmit` ou o…

</details>

<a id="mods"></a>

## Mods: criados com a capacidade de modificação

Cada entrada aqui apresenta evidências do uso da capacidade que o Claude Code adquiriu na versão 2.1.287: ela desenha por meio de `ui.render`, possui um painel, faixa ou cartão, lê `$.ui.selection()`, cria companheiros de equipe com `agent.spawn` ou afirma claramente que é um mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2535 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Encontre os tokens fantasmas. Corrija-os. Sobreviva à compactação. Evite a degradação da qualidade do contexto.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | Python                                                                |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2535**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐493 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Catálogo comunitário de mods públicos do Claude Code (hooks de função), varridos de GitHub, com o que cada mod pode ler, escrever, executar ou enviar pela rede. Navegue por https://mods.aidojo.si/

<sub>🔧 Encontrado em uso no código: `data/seeds.txt`, `README.md`, `data/repos.txt`, `finder/README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **493**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐187 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mods do Claude Code: plugins baseados em hooks que adicionam linhas em tempo real acima do prompt, proteções, painéis e jogos. Barra de contexto, medidor de uso, monitoramento de revisão do Codex, visualização de Markdown, música atual do Spotify e muito mais.

<sub>🔧 Encontrado em uso no código: `mods/next-steps/hooks/register.tsx`, `mods/agent-radar/hooks/register.tsx`, `mods/review-watch/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **187**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐137 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Mantenha o cache de prompt do Claude Code aquecido durante as pausas e mostre o custo estimado antes de um envio a frio.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **137**    |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/9ba5b1dbc9440791.png" width="100%" alt="karanb192/cache-tax screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/karanb192--cache-tax/e1a7cdd41b0efd1b.gif" width="100%" alt="karanb192/cache-tax animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/karanb192/cache-tax/main/docs/assets/cache-cost-explainer.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/awss1i/assay">awss1i/assay</a></b> · ⭐104 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Um CLI de QA nativo para agentes em páginas da Web. Determinístico, sem necessidade de escrever testes e sem LLM.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | HTML                                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **104**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `agentic-ai` · `ai-agents` · `browser-automation` · `claude-code` · `claude-code-mod` · `cli` · `code-generation` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐80 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code exibe imagens e reproduz vídeos diretamente no terminal: capturas de tela, gravações do Playwright e QA sincronizado de antes / depois. Ghostty e kitty.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **80**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐78 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Uma coleção de mods para claude code

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **78**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐76 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Respostas coloridas e personalizáveis do Claude Code: tabelas, código, diagramas, gráficos e linhas de ferramentas em 15 temas, com botões de cópia. Um mod do Claude Code.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **76**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/9df6377936558503.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐67 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Um mod do código Claude que coloca um painel de agente ao vivo no seu terminal: contexto e custo, linha do tempo do consultor, cada verificação de permissão, cartões de subagentes e raias.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **67**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 5 天</summary>

##### 📝 Summary

Mods do Claude Code criados por Darrell Wang — faixas acima do prompt, sem tokens do modelo. Painel de ações de Taiwan／EUA + mais novidades em breve.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | HTML                                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **65**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐59 · Shell · 👁️ observed · 4 天</summary>

##### 📝 Summary

Skills, agentes, comandos, regras, hooks e estilos de saída especializados para Claude Code — continuidade de sessão + ferramentas modernas de CLI para fluxos de desenvolvimento do mundo real

<sub>🔧 Encontrado em uso no código: `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | Shell                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **59**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐50 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Coleção de mais de 100 mods que você pode usar com Claude Code.

<sub>🔧 Encontrado em uso no código: `README.md`, `docs/COMMUNITY_MODS.md`, `mods/agent-board/hooks/register.js`, `mods/desktop-agent-desk/hooks/register.js`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **50**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐46 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Mods do Claude Code: barras de progresso do plano em tempo real acima do prompt

<sub>🔧 Encontrado em uso no código: `README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **46**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Veja o Claude Code fabricar um pequeno desenho animado enquanto você trabalha.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **32**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-10 |

🏷 `ai-narration` · `claude` · `claude-code` · `claude-code-plugin` · `claude-mod` · `claude-mods` · `developer-tools` · `fun`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/283c6335f0455468.png" width="100%" alt="henrik-thevibe/Claude-Fables screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/henrik-thevibe--claude-fables/630db5cb89b1339d.gif" width="100%" alt="henrik-thevibe/Claude-Fables animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐27 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Uma barra com os prompts da sua sessão do Claude Code: passe o mouse para ler, clique para acessar (hooks de função / Mods)

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **27**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐25 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Um Pokémon em pixel que vive acima do prompt no Claude Code

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/dgokcin/claude-pokemon-mod/main/gifs/pikachu-haiku.gif" width="100%" alt="dgokcin/claude-pokemon-mod animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐23 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Uma transformação do Claude Code: painel de cockpit ao vivo, temas compartilháveis e um mascote em pixels que encena o que Claude está fazendo

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Build, testes, console e prévias do SwiftUI do Xcode dentro do Claude Code

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mods` · `claude-code-plugin` · `ghostty` · `ios` · `mcp` · `swift` · `swiftui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/artemnovichkov--xcode-mods/bc34e8dd0f730ea2.png" width="100%" alt="artemnovichkov/xcode-mods screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Mods do Claude Code: 21 estilos e um conjunto completo de recursos que você ativa quando precisar, para o terminal e o aplicativo para desktop. · Dê um novo estilo ao Claude com um clique e tenha um conjunto completo de recursos ativados sob demanda.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins` · `developer-tools` · `mods` · `pixel-art` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/lemomo-ai--lemo-mod/d6e9ce6141976f64.png" width="100%" alt="lemomo-ai/lemo-mod screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 9 天</summary>

##### 📝 Summary

Dez mods do Claude Code, guias para iniciantes, prompts de criação, demonstrações seguras e um template para criar o seu próprio.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **20**     |
| Last push    | 2026-10-02 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/promptadvisers/claude-mods-starter-kit/main/assets/cover.jpg" width="100%" alt="promptadvisers/claude-mods-starter-kit screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Mods do Claude Code: usage-band mostra seus limites de 5h/7d, a janela de contexto e a taxa de acertos do cache acima do prompt

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **13**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐11 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Mods do Claude Code que tornam as perguntas de Claude mais fáceis de ler e responder (qa-guide).

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `askuserquestion` · `claude-code` · `claude-code-plugin` · `mod`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/e57e7bee7cb5c173.png" width="100%" alt="aieo-product/claude_qamods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aieo-product--claude_qamods/eb4a2b15bdb5ff3e.gif" width="100%" alt="aieo-product/claude_qamods animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/aieo-product/claude_qamods/main/docs/media/qa-guide-pv-16x9.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐11 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mod do Claude Code: contexto em tokens, limites de 5 horas e semanais em relação ao relógio, contagem regressiva do cache de prompt, custo da sessão e agentes em execução, tudo em uma faixa acima do prompt.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Dez mods de código aberto para Claude Code: painéis em tempo real, faixas, linhas de status e proteções para chamadas de ferramentas. Medidor de consumo, launch codes, sessão encerrada, boss fight, mascote de código e muito mais.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/onewave-ai--claude-code-mods/763e0352f43b1cbc.png" width="100%" alt="OneWave-AI/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐11 · JavaScript · 👁️ observed · 6 天</summary>

##### 📝 Summary

Dois mods do Claude Code: ponte de uso do computador de Codex e sessões coordenadas de Claude. Código-fonte, prompts de build, configuração e testes.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **11**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Pixel art animada acima do seu prompt do Claude Code, que reage enquanto Claude trabalha. Sete cenas, ou sua própria imagem ou GIF. Zero tokens.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **10**     |
| Last push    | 2026-10-04 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 26 天</summary>

##### 📝 Summary

Rastreadores de sessão para o Claude Code criados como mods: janela de contexto, consumo da cota do plano e custo por turno

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-09-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `developer-tools` · `function-hooks` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Arunjay4213/claude-mods/main/docs/demo.gif" width="100%" alt="Arunjay4213/claude-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Uma interface para seus terminais do Claude Code e Codex, criada pelos seus agentes, para que o único modelo na sua cabeça seja o seu.

<sub>🔧 Encontrado em uso no código: `CLAUDE.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

KOZMOS — mods visuais ao vivo para Claude Code (CLI + desktop): faixas acima do prompt, barras laterais, ticker de status, companheiros, guardas e som.

<sub>🔧 Encontrado em uso no código: `mods/compass/README.md`, `mods/blackbox/README.md`, `mods/orrery/README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `tui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ersinkoc--claude-mods/ece950c6b8ad049e.png" width="100%" alt="ersinkoc/claude-mods screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Seis mods de Claude Code em um único plugin (Token Weather, Cache Keeper, Wait What, Prompt Queue, Snake, Blast Radius), com alternâncias por mod, além de um relatório mods versus hooks.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/az9713--claude-mod-pack/7889282e792ed11e.png" width="100%" alt="az9713/claude-mod-pack screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 7 天</summary>

##### 📝 Summary

Coleção de mods de Claude Code do 개발동생. Pacote táxi: taxímetro, navegação, câmera de fiscalização de velocidade e câmera veicular

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Assistir em youtube.com</a> · a reprodução é aberta no site de origem; GitHub não pode incorporá-la em linha</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/nogu66/md-prompt">nogu66/md-prompt</a></b> · ⭐7 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Markdown aplicado à caixa de prompt do Claude Code enquanto você digita. Código delimitado se torna um cartão com destaque de sintaxe antes mesmo de você fechar o delimitador.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-03 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/b729912bc80aeee4.png" width="100%" alt="nogu66/md-prompt screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nogu66--md-prompt/408107e3aa381332.gif" width="100%" alt="nogu66/md-prompt animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ronanworks/claude-code-mods">ronanworks/claude-code-mods</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Mods de Claude Code: painel de uso 像素螃蟹 usage-hud + links HTML clicáveis no terminal e cartões html-shelf de código com cópia em um clique

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ronanworks--claude-code-mods/c6d323f2b976bd4e.gif" width="100%" alt="ronanworks/claude-code-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/arasovic/claude-code-mods">arasovic/claude-code-mods</a></b> · ⭐6 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mods para o Claude Code: plugins de function-hook que adicionam painéis dinâmicos e comportamento à interface de terminal

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-10 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arasovic--claude-code-mods/a8e330d8ce6f7bad.png" width="100%" alt="arasovic/claude-code-mods screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 430</sub></summary>

- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods do Claude e as ferramentas para criá-los: primeiro uma skill de criação…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - O harness do Claude Code que uso todos os dias, publicado com este nome desde o…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Troque o telhado do Claude Code usando Claude Mods: sem alterar o binário…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatro mods do Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods do Claude Code do Learning Hacker: transforme o funcionamento do agent em…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods do Claude Code que corrigem e traduzem seus prompts antes que Claude os…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods e skills de Claude Code do Nekyia Labs, criados e usados diariamente por…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Uma aparência de aplicativo desktop para a transcrição do terminal do Claude…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Um painel lateral para o código Claude: os subagentes executados por uma…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conhecimento do Obsidian com fontes citadas sobre Claude Code mods…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Painel lateral do Claude Desktop (aba Code): lista todos os afazeres inacabados…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill que ensina agentes do Claude Code a criar Claude Mods.
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso acima da caixa de entrada do Claude Desktop (aba Code): cota de 5h…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins e skills comunitários do Claude, instaláveis em um único mercado.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de hooks de função) para Claude Code.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - A galeria de mods do Baselane: mods de Claude Code, verificados e fixados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Uma fila de decisões CLI/TUI para humanos que trabalham com agentes…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Um cartão de status flutuante para o Claude Code — modelo, contexto, limites de…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nomes e segredos enquanto você…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Painel GSD ao vivo para Claude Code: roadmap, árvore de agentes com…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensões do Claude Code. Desbloqueie todo o poder do Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) do Claude Code que adiciona um painel lateral com abas Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Painéis, proteções e mods de qualidade de vida para Claude Code: contexto, uso…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dois mods de Claude Code acima da caixa de prompt: medidor da janela de…
- [VedantAndhale/claude-pro-kit](https://github.com/VedantAndhale/claude-pro-kit) - Faça o plano Claude Pro durar mais: mods de Claude Code para um HUD de uso…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Leia os arquivos Markdown nomeados pelo código Claude, renderizados ao lado da…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Colega de trabalho por voz para o Claude Code.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, um velocímetro de digitação ao vivo com…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fogos de artifício para o Claude Code: cada tecla pressionada, chamada de…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubra mods, plugins e extensões de Claude Code com demonstrações animadas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas mermaid desenhados diretamente na transcrição.
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods and skins for Claude Code: a live progress bar for Claude.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequenos mods do Claude Code (plugins de function-hook): session-switcher e mais.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imagens coladas acima do prompt, em qualquer…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods de Claude Code: menu de ferramentas Claude, modo Zen, temas de terminal…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encontre os mods que você mais usaria)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dois mods de Claude Code para executar muitas sessões simultaneamente: um…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubra, inspecione, alterne e atualize mods de Claude Code.
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, painel de agentes, desfoque PDPA.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Melhores mods de Claude Code: selecionados, validados e fixados.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin do Claude Code: roteamento automático de modelos Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascote Clawd animado, barras de limite de uso e…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Um marketplace de mods para Claude Code: depurador passo a passo para o loop do…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: limites do plano e contexto acima do prompt, um…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - O melhor pacote de mods completo para o Claude Code: limites de uso e HUD de…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Assista a YouTube Shorts no seu Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de ferramentas de Naren para Claude: skills, mods e servidores MCP para o…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod do Claude Code que desenha diffs de Edit e Write em duas colunas lado a lado.
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, um pequeno mascote pixelado que representa o que…
- [reporails/arcade](https://github.com/reporails/arcade) - Jogos clássicos de desktop como mods de Claude Code, jogados em um painel…
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Uma lista selecionada de mods de código do Claude, instaláveis como um…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de código do Claude sob demanda — uma habilidade que lê sua conversa e…
- [xsyetopz/dotclaude](https://github.com/xsyetopz/dotclaude) - Um plugin bastante opinativo para Claude Code, desenvolvido por um Rustacean…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantêm um agente honesto — hooks de função que protegem…
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - Minha coleção de mods do Claude Code, um mod por diretório.
- [ArgonQQ/sipp](https://github.com/ArgonQQ/sipp) - 💧 Um lembrete de água passivo-agressivo para o Claude Code.
- [bostonaholic/claude-mods](https://github.com/bostonaholic/claude-mods) - The Claude Code mods I use.
- [chenyuxiaojin/cyxj-notch](https://github.com/chenyuxiaojin/cyxj-notch) - Dashboard notch do macOS para o Claude Code: limites de uso, sessões abertas…
- [Danovich/turntype](https://github.com/Danovich/turntype) - A typing test for the time while Claude works. A Claude Code mod.
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod para o Claude Code: barra de cache de prompts, próximos passos, botões…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para o Claude Code: painéis, comandos e hooks criados com o plugin…
- [drkokorev/context-diet](https://github.com/drkokorev/context-diet) - Trims huge tool outputs before they fill Claude Code.
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Um mod do Claude Code que desenha seus limites de uso e gastos na faixa acima…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods do Claude Code de Herman (marketplace herman-mods).
- [homieyangg/claude-code-mods](https://github.com/homieyangg/claude-code-mods) - Mods do Claude Code: barras de progresso para planos, um registro do que Claude…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Veja o que o Claude Code executa em segundo plano: subagentes, tarefas do…
- [macleodlabs-ai/claudeflow](https://github.com/macleodlabs-ai/claudeflow) - Claude Code mods by MacLeod Labs: streams untangles a session.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo do primeiro dia sobre mods do Claude Code no Windows: uma barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods que criei e uso pessoalmente na minha configuração do Claude Code.
- [olddonkey/cache-refresher](https://github.com/olddonkey/cache-refresher) - Claude Code mod: shows when the prompt cache expires and what a lapse would…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod do Claude Code: medidores ao vivo de custo, contexto e cota do plano acima…
- [rbartoli/agent-usage-guard](https://github.com/rbartoli/agent-usage-guard) - Um mod de Claude Code que retém a ramificação de subagentes, prompts com…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Um mod do Claude Code que ativa ou desativa suas habilidades, agentes, regras e…
- [simplecore-inc/claude-mods](https://github.com/simplecore-inc/claude-mods) - Plugins (mods) do Claude Code: alterne entre várias contas do Claude, acompanhe…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods do Claude Code testados e instaláveis com um comando: proteções para o…
- [Sma1lboy/claude-mods](https://github.com/Sma1lboy/claude-mods) - Mods para o Claude Code: plugins criados com function hooks.
- [smukh/roll-credits](https://github.com/smukh/roll-credits) - Créditos em estilo de filme para sua sessão de programação.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace dos meus mods do Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Vários mods do claude code criados por mim.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods do Claude Code. touch-map: veja quais arquivos Claude listou, leu, editou…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprenda um idioma estrangeiro enquanto trabalha com o código Claude.
- [alaturqua/tower-mods](https://github.com/alaturqua/tower-mods) - Mods de Claude Code para executar muitas sessões em muitos repos a partir de…
- [alexlifexyz/p3c-guard](https://github.com/alexlifexyz/p3c-guard) - Quando o Agent escreve Java, código que viola as regras Alibaba Java (p3c) não…
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de custo, tokens e uso de contexto ao vivo para Claude Code: um…
- [aosmcleod/next-up-mod](https://github.com/aosmcleod/next-up-mod) - Mod do Claude Code: um backlog dos acompanhamentos que Claude sugere em todas…
- [atharv6f/headway](https://github.com/atharv6f/headway) - Goal, tasks and agents above your Claude Code prompt — zero setup.
- [BjoernSchotte/ccmod-amp](https://github.com/BjoernSchotte/ccmod-amp) - Rádio pela Internet dentro do Claude Code: uma barra lateral cliamp, mini…
- [Bocskay-Botond/claude-code-mods](https://github.com/Bocskay-Botond/claude-code-mods) - Mods divertidos e úteis de Claude Code: uma criatura em pixel acima do seu…
- [CalvoSeko/claude-factory-mod](https://github.com/CalvoSeko/claude-factory-mod) - agent-graph: um mod do Claude Code para projetar e executar grafos de agentes…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - Claude está cozinhando. Converse com seu esquadrão.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods do Claude Code para Engineers de verdade.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Claude Code&#x27;s terminal session recap, in the Claude desktop app&#x27;s Code tab.
- [darkomarijaan/nexus-mod](https://github.com/darkomarijaan/nexus-mod) - Mod completo do Claude Code: HUD ao vivo, proteções de segurança.
- [DarkVelours/claude-code-galactic-battle](https://github.com/DarkVelours/claude-code-galactic-battle) - Uma batalha espacial acima do prompt do Claude Code enquanto ele trabalha.
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Veja quais arquivos cada agente do Claude Code tem em seu contexto, e quanto de…
- [drakulavich/cogload](https://github.com/drakulavich/cogload) - Mantenha a cabeça fria. Um termômetro para seus dias no Claude Code: cada hora…
- [EgonLeitner/dashband](https://github.com/EgonLeitner/dashband) - Cache de prompts, contexto e limites do plano em uma visão geral para o Claude…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequenos mods do Claude Code para o terminal e o aplicativo desktop.
- [erte-del/claude-mods](https://github.com/erte-del/claude-mods) - Claude Code mods (plugin marketplace): live sidebar with context, cost and…
- [ewxgwy1987/claude-code-progress-board](https://github.com/ewxgwy1987/claude-code-progress-board) - Mod de Claude Code: painel de progresso para tarefas, subagentes, execuções de…
- [ewxgwy1987/claude-code-session-toc](https://github.com/ewxgwy1987/claude-code-session-toc) - Mod de Claude Code: sumário clicável e com marcas de tempo de toda a sessão…
- [ewxgwy1987/claude-code-usage-meter](https://github.com/ewxgwy1987/claude-code-usage-meter) - Mod de Claude Code: limites de taxa do plano, preenchimento do contexto, custo…
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidade + mod Claude CLI que adiciona palavras em espanhol às respostas do…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Seus eventos do Alarum acima do prompt do Claude Code: o que acabou de chegar e…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Seu backlog Floatee acima do prompt do Claude Code: execute, guie e marque seus…
- [gonzalonicolasr/claude-code-nerv](https://github.com/gonzalonicolasr/claude-code-nerv) - Barra lateral no estilo Evangelion para Claude Code: contexto, cota, atividade…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Um mod de código do Claude que o reformula como The Machine de Person of…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod do Claude Code para fluxos de trabalho DAG obrigatórios e…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código de código aberto para o Claude Code: painéis, linhas de status…
- [jduerrmann/agent-crew](https://github.com/jduerrmann/agent-crew) - Um mod de código do Claude: um painel para cada subagente, os arquivos que eles…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod do Claude Code: status da sessão, progresso ao vivo do Spec Kit e…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - A janela de contexto como uma linha acima do prompt, desenhada da forma como o…
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Um HUD de tarefas ao vivo para o Claude Code Desktop: uma faixa acima do prompt…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Um plugin gratuito e de código aberto para Claude Code.
- [maxsoldev/pstash](https://github.com/maxsoldev/pstash) - Guarde prompts para mais tarde e coloque-os de volta na caixa de entrada do…
- [Mechazawa/claude-inline-images](https://github.com/Mechazawa/claude-inline-images) - Mod de Claude Code que mostra imagens inline no Ghostty e no kitty.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - Um Mod do código Claude que mostra as solicitações de pull GitHub da sessão em…
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nkapila6/sfx-gen](https://github.com/nkapila6/sfx-gen) - Mod do Claude Code: gere efeitos sonoros a partir de prompts de texto com um…
- [NMenzel/claude-devtools-mod](https://github.com/NMenzel/claude-devtools-mod) - Claude DevTools: a debugger for Claude Code tool calls.
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Skills do Claude Code: verificador de fatos para documentos, auditor de código…
- [pepperonas/loc-today](https://github.com/pepperonas/loc-today) - Mod do Claude Code: linhas de código de hoje por Claude — novas, editadas e…
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod de Claude Code: caminhos clicáveis nas respostas — clique em uma pasta para…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin de companheiro do código Claude: um companheiro ASCII acima do seu…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Mod de Claude Code: roteamento de modelo/esforço guiado por Jev, compactação de…
- [samfrmr/barmkin-mod](https://github.com/samfrmr/barmkin-mod) - Claude Mods do Code: camada de segurança para o Claude Code — ocultação de…
- [seanrobertwright/claude-mods](https://github.com/seanrobertwright/claude-mods) - A collection of Claude Code mods.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod do Claude Code: um SDLC nativo de IA.
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Coleção incrível de mods do Claude Code | Coleção de mods do Claude Code.
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 Um mod de HUD de RPG aconchegante para o Claude Code.
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Mods do Claude Code: painéis ao vivo e hooks para o trabalho diário.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: um mod de Claude Code que lê em voz alta as respostas de Claude e…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Dê uma palmada em Claude quando ele fizer besteira — um mod de alívio do…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods do Claude Code: pequenos plugins para painéis ao vivo, roteamento de…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin do Claude Code: monitor de uso, rastreador de tokens e linha de…
- [VictorGambarini/jev-mod](https://github.com/VictorGambarini/jev-mod) - A Claude Code mod that hands the small decisions to a cheap decision model…
- [yuntaengtaeng/snitch](https://github.com/yuntaengtaeng/snitch) - Mod de código do Claude que informa quais arquivos Claude alterou e por quê, o…
- [afterever/claude-mods](https://github.com/afterever/claude-mods) - Claude Code mods by afterever (plugin marketplace).
- [ajkatom/claude-mods](https://github.com/ajkatom/claude-mods)
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [alan-oliv/claude-mods](https://github.com/alan-oliv/claude-mods) - Mods do Claude Code: cartões de estatísticas da sessão acima do prompt.
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Um gato de braille animado acima do prompt do Claude Code.
- [alinaqi/mixture-of-models-claude-mod](https://github.com/alinaqi/mixture-of-models-claude-mod) - Mod do Claude Code: direciona tarefas baratas para GLM/Kimi por meio de um…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Um gato em pixel acima do seu prompt do Claude Code que executa uma chamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Um mod do Claude Code que escolhe um bom momento para compactar e manter…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods Claude para o Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Marketplace de plugins do Claude Code por anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de uso geral para o Claude Code: faixas, painéis, toasts e hooks.
- [arslan-charyyev/claude-mods](https://github.com/arslan-charyyev/claude-mods) - My private Claude Code mods.
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - O navio LGTM Lines passa navegando após cada alteração de código — um mod do…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Seus limites de uso do Claude como um cartão de saúde de aldeão animado, com um…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [astrosteveo/plain-english](https://github.com/astrosteveo/plain-english) - A Claude Code mod that makes Claude write plain English and flags its usual…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Treinos curtos enquanto Claude trabalha: uma meta diária, sequências…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Um painel de uso para o código Claude: gastos por modelo.
- [barneym/claude-context-bar](https://github.com/barneym/claude-context-bar) - Um mod do Claude Code: detalhamento do contexto da janela ao vivo acima do…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para o código Claude: Apple Music e Spotify acima do prompt…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: relógio de cache, raio de impacto, sugestões, lista de…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Apenas uma coruja para o seu Claude Code.
- [cesarroger/skill-deck](https://github.com/cesarroger/skill-deck) - A Claude Code mod: keep skills manual-only and switch them on in profiles, per…
- [cGradying/claude-code-cockpit](https://github.com/cGradying/claude-code-cockpit) - Faixa de uma linha do Claude Code.
- [chamonkey-crypto/claude-mods](https://github.com/chamonkey-crypto/claude-mods)
- [ChaseWNorton/claude-doom](https://github.com/ChaseWNorton/claude-doom) - O mecanismo original Doom com Freedoom, jogável dentro do Claude Code.
- [chshin84/claude-mods](https://github.com/chshin84/claude-mods) - Claude Code 단어 사전 패널과 상태 표시줄 플러그인.
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Um mod do Claude Code que mantém uma lista contínua dos itens em aberto em uma…
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Revise todos os arquivos tocados por Claude, como em um pull request, sem sair…
- [dalemorgan04/claude-mods](https://github.com/dalemorgan04/claude-mods) - Claude Mods.
- [darshk07/claude-mods](https://github.com/darshk07/claude-mods)
- [davidparys/claude-mods](https://github.com/davidparys/claude-mods) - Claude Code mods: rule-keeper saves your corrections as permanent rules.
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Um Tamagotchi que vive dentro do Claude Code: ele eclode, come o código que…
- [dbroadhurst/claude-mod-goal](https://github.com/dbroadhurst/claude-mod-goal) - A Goal pane for Claude Code: the overall goal Claude is working toward, why…
- [densi97/claude-code-command-log](https://github.com/densi97/claude-code-command-log) - Claude Code Mod to explain commands ran by the agent.
- [devohmycode/ccmods](https://github.com/devohmycode/ccmods) - Mods do Claude Code escritos como hooks de função e o marketplace que os…
- [diamondT/claude-mods](https://github.com/diamondT/claude-mods)
- [dieg666/claude-herald](https://github.com/dieg666/claude-herald) - A Claude Code mod: a band above the prompt with Claude news and the breaking or…
- [dot-agi/arrester](https://github.com/dot-agi/arrester) - Mod do Claude Code: depois que um guard bloqueia uma chamada de ferramenta, ele…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Mod do Claude Code: tarefas em segundo plano em uma única visualização, com…
- [dot-agi/high-command](https://github.com/dot-agi/high-command) - Mod do Claude Code: uma única caixa de entrada para mensagens de colegas de…
- [dot-agi/sandbox-tuner](https://github.com/dot-agi/sandbox-tuner) - Mod do Claude Code: explica bloqueios do sandbox e transforma bloqueios…
- [DragosMocrii/proc-stats](https://github.com/DragosMocrii/proc-stats) - Claude Code mod: status line with the session.
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoritos para Claude Code: ícones de um clique para seus comandos e habilidades.
- [Dyarchia/dyarchia](https://github.com/Dyarchia/dyarchia) - Dyarchia: Build and Kanban on every surface.
- [Egrn/claude-code-mutedit](https://github.com/Egrn/claude-code-mutedit) - Ei, silenciou! Abandone o diff, corte o riff, sem mais edições, menos créditos.
- [Eiyuo/Claude-Mods](https://github.com/Eiyuo/Claude-Mods)
- [ekinertac/claude-code-mods](https://github.com/ekinertac/claude-code-mods) - Claude Code mods: rewrite-prompt (Ctrl+P rewrites your draft before you send it).
- [elijah-rou/agent-kit](https://github.com/elijah-rou/agent-kit) - Instructions, skills, Pi extensions, and Claude Code mods for Pi, Codex, and…
- [EmanueleNene/claude-mods](https://github.com/EmanueleNene/claude-mods) - Claude Modificações de código: delete-guard (confirma exclusões de arquivos) e…
- [eric1hua/claudemods-desktop-statusline](https://github.com/eric1hua/claudemods-desktop-statusline) - Mod do Claude Code: uso da assinatura (5h / 7d) como uma faixa acima do prompt…
- [fatihkartal35/claude-mods](https://github.com/fatihkartal35/claude-mods) - Claude Code mods: auto-model-detector routes each prompt to the right model and…
- [floheissler/cc-worktree-radar](https://github.com/floheissler/cc-worktree-radar) - Um radar ao vivo dos seus branches e worktrees paralelos acima do prompt: quais…
- [Gat0rRex/claude-mods](https://github.com/Gat0rRex/claude-mods) - Claude Code mods (function-hook plugins): context band, loose ends, checkpoint…
- [Gharib89/claude-mods](https://github.com/Gharib89/claude-mods) - Modificações de código do Claude (plugins de function-hook), instaladas por…
- [gomymy64/claude-code-mods-cheatsheet](https://github.com/gomymy64/claude-code-mods-cheatsheet)
- [gotzastory/my-mods](https://github.com/gotzastory/my-mods) - Mods do Claude Code: context-bar-plus.
- [hahahahahahahahah6/mod-audit](https://github.com/hahahahahahahahah6/mod-audit) - Static supply-chain auditor for Claude Code Mods — local, offline, stdlib-only.
- [hahahahahahahahah6/task-progress-mod](https://github.com/hahahahahahahahah6/task-progress-mod) - Claude Code Mod: live TodoWrite progress bar above the prompt.
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de código do Claude: quanto tempo cada resposta levou, quanto tempo Claude…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Modificações de código do Claude: streamer-mode oculta painéis privados, bandas…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [iceberggymnast/claude-code-mods](https://github.com/iceberggymnast/claude-code-mods) - Plugins de function-hook do Claude Code (mods).
- [icedevil2001/auto-continue](https://github.com/icedevil2001/auto-continue) - Mod do Claude Code: espera o limite de uso de 5 horas passar e envia &quot;continue&quot;…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Um cockpit acima do seu prompt do Claude Code. O pato lê os medidores.
- [ipartington/claude-mods](https://github.com/ipartington/claude-mods) - Claude Code mods (function-hook plugins): PR merge follow-through, /clear…
- [jakerains/claudemods](https://github.com/jakerains/claudemods) - Small Claude Code mods: context and plan-usage gauges, a prompt-cache meter…
- [jamesnguyen1309/claude-usage](https://github.com/jamesnguyen1309/claude-usage) - Claude Code mod: live token usage, models and subagents per prompt.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Painel de uso do contexto na barra lateral: total, categorias, crescimento por…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista de arquivos na barra lateral: quais arquivos foram criados, modificados…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, um coelho holandês anão preto e branco em estilo 8-bit, corre e pula acima…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - A seção “O que eu perguntei” na barra lateral: cada frase que o usuário digitou…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linha do tempo na barra lateral: onde o tempo desta rodada foi gasto.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Movimentação de tokens na barra lateral: quantos tokens a conversa principal…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - O “confessionário honesto” do claude code: após responder em cada rodada…
- [jimmysteinmetz/b-sides](https://github.com/jimmysteinmetz/b-sides) - Pequenos mods para Claude Code, como novos comandos de barra e painéis laterais.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive em uma faixa acima do prompt do Claude Code: encena a sessão, mostra…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Mod que lê em voz alta as respostas e notificações do Claude Code usando…
- [kbrdn1/claude-crosstalk](https://github.com/kbrdn1/claude-crosstalk) - Um mod do Claude para ler e participar das conversas entre suas sessões do…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods do Claude Code. PixBar: uma criatura pixelada acima do seu prompt que se…
- [kkatsuyoshi/claude-mods](https://github.com/kkatsuyoshi/claude-mods) - claude mods.
- [KKK12142/claude-mods](https://github.com/KKK12142/claude-mods) - Modificações de código do Claude (usage-meter, ...).
- [koenrohrer/hearth-band](https://github.com/koenrohrer/hearth-band) - Claude Code mod: a pixel creature per model beside a prompt-cache campfire…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Dois mods de código do Claude: folio, um painel de arquivos ao lado do chat, e…
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: um gráfico ao vivo do que o Claude Code sabe.
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Não deixe sua atenção se dispersar enquanto espera pela resposta do Claude Code.
- [linsanmufilm-svg/claude-mods](https://github.com/linsanmufilm-svg/claude-mods) - Mods do Claude Code de Sanmu — um marketplace de plugins.
- [LordMordelon/claude-mods](https://github.com/LordMordelon/claude-mods) - Mods de Claude Code para los proyectos de Angel (Vremia).
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Um guia de Mods do Claude Code organizado pela comunidade: casos de uso…
- [LupusMalusDeviant/claude-mods](https://github.com/LupusMalusDeviant/claude-mods) - Single Claude Code mods from the Mod Box, each installable on its own.
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Um mod do Claude Code que mostra o que Claude está fazendo no subtítulo da aba…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Uma gata preta e fofa acima do prompt do Claude Code.
- [MarcusJellinghaus/claude-mode-gate](https://github.com/MarcusJellinghaus/claude-mode-gate) - Um mod do Claude Code com perfis de permissões alternáveis: uma linha de base…
- [Mark-Hickey/claude-nine](https://github.com/Mark-Hickey/claude-nine) - Claude Code mods: Linear + PR watch, cortex mesh toasts, safe repo sync.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Small mods for Claude Code: runner-avatar, a little avatar that runs above your…
- [Marnel8/claude-mods-](https://github.com/Marnel8/claude-mods-)
- [martin-macak/claude-code-mod-tracking](https://github.com/martin-macak/claude-code-mod-tracking) - Claude Code mod for tracking related artifacts and references.
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Claude Code mod: a live pane of the agent.
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods da comunidade para o Claude Code: proteções, painéis e comandos executados…
- [michaelblaess/turbo-mod](https://github.com/michaelblaess/turbo-mod) - Painel lateral para o Claude Code: arquivos escritos por Claude, divisões do…
- [micke-dahlgren/token-range-monitor](https://github.com/micke-dahlgren/token-range-monitor) - Mod do Claude Code: projeta o que restará dos seus limites semanais e de 5…
- [mmedum/glimt](https://github.com/mmedum/glimt) - Um painel lateral discreto para Claude Code: o que esta sessão está fazendo…
- [mmedum/nuet](https://github.com/mmedum/nuet) - Um horário esmaecido acima de cada prompt e de cada resposta na transcrição do…
- [mmedum/spor](https://github.com/mmedum/spor) - Recoloca o que o Claude Code oculta: os arquivos que Claude leu, os comandos…
- [mrkshw/cold-cache](https://github.com/mrkshw/cold-cache) - Claude Code mod: warns when a session.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod do Claude Code que reativa as ferramentas de tarefas pendentes para modelos…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod do Claude Code que espera uma pausa segura e então transfere sua sessão ou…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod do Claude Code: uma linha por tarefa acima do prompt com a tarefa atual…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jogue Connect Four contra uma AI dentro do Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: quando outro agente de programação faz commit no seu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositórios compartilhados por vários agentes de IA…
- [Nelahia/claude-mods](https://github.com/Nelahia/claude-mods) - Installe et configure mes mods Claude Code en une commande.
- [NeonOrchard/tab-alert](https://github.com/NeonOrchard/tab-alert) - Claude Code mod: flashes the terminal tab while Claude waits on you.
- [nerevar48/nerevar-mods](https://github.com/nerevar48/nerevar-mods) - Marketplace de mods do Claude Code.
- [netgfx/claude-flow-explainer](https://github.com/netgfx/claude-flow-explainer) - A Claude mod to guide the user step by step on how a flow or code works.
- [NicBritz/claude-code-mods](https://github.com/NicBritz/claude-code-mods) - Mods divertidos e gratuitos para o Claude Code que nunca gastam um token.
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Uma proteção para SQL no Claude Code: pergunta antes que Claude execute DELETE…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Um mod para Claude Code, Windows e CJK em primeiro lugar: prévias de imagens e…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [Orbitmap/claude-mods](https://github.com/Orbitmap/claude-mods) - Claude Code mods made by the OrbitMap team.
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Os melhores Mods do Claude Code, classificados pelo que fazem por você.
- [pakornkub/session-insight](https://github.com/pakornkub/session-insight) - Claude Code mod: session usage, skills and agents, with an agent diagram.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dois Mods do Claude para o Claude Code: guarda-corpo.
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [paragpandyareal/swear-slap](https://github.com/paragpandyareal/swear-slap) - Xingue o Claude Code e uma mão de desenho animado responde com um tapa.
- [paulosergio-jnr/claude-code-mods](https://github.com/paulosergio-jnr/claude-code-mods) - Claude Code Mods repo.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Painel lateral de estatísticas de sessão em tempo real para a aba Code do…
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods para o Claude Code: safety-guard bloqueia comandos destrutivos e acesso a…
- [ptsnac/claude-session-handoff](https://github.com/ptsnac/claude-session-handoff) - Claude Code mod: session timer and one-click handoff to a fresh context window.
- [rajib2k5/claude-market-watch](https://github.com/rajib2k5/claude-market-watch) - Mod de Claude Code: ticker de ações ao vivo, painel /quote, alertas de preço…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [ray-amjad/cache-clock](https://github.com/ray-amjad/cache-clock) - Mod do Claude Code: uma faixa acima do prompt mostrando o contexto usado e uma…
- [ray-amjad/diagram-pane](https://github.com/ray-amjad/diagram-pane) - Mod do Claude Code: um painel lateral que fixa cada diagrama que Claude desenha…
- [ray-amjad/dream-pass](https://github.com/ray-amjad/dream-pass) - Mod do Claude Code: uma etapa de sonho que mescla, reescreve e poda a pasta de…
- [ray-amjad/prompt-bouncer](https://github.com/ray-amjad/prompt-bouncer) - Mod do Claude Code: elimina prompts vagos antes que Claude os veja e sugere o…
- [ray-amjad/secret-box](https://github.com/ray-amjad/secret-box) - Claude Code mod: Claude uses your secrets without seeing them.
- [ray-amjad/transcript-redactor](https://github.com/ray-amjad/transcript-redactor) - A Claude Code mod that keeps secrets out of the session transcript: every key…
- [RedRoosterKey/claude-code-ssh-usage-band](https://github.com/RedRoosterKey/claude-code-ssh-usage-band) - Mod de Claude Code: host SSH, RAM e limites de uso de 5h/7d em uma linha acima…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod do Claude Code: flexões para fazer enquanto Claude trabalha. Sem tokens.
- [robinade/claude-mods-ko](https://github.com/robinade/claude-mods-ko) - Claude Code mod 한국어판 6종: 가정 기록, 쉬운 말, 아이디어 선반, 프롬프트 다듬기, 세션 모니터·트래커.
- [rogadev/paceline-mod](https://github.com/rogadev/paceline-mod) - paceline as a Claude Code mod: paces your usage limits in a line above the…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods para claude code.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod do Claude Code: transforma o plano que você aprova no modo de planejamento…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Uma lista selecionada de mods do Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sem custo: os agentes auxiliares rodam no Haiku, e arquivos grandes e logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Uma trilha sonora lofi que acompanha a sessão: calma, foco, fluxo, além de…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprenda enquanto Claude programa: após um turno que alterou o código, uma…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Uma gravação de cada edição feita por Claude: reproduza cada alteração sendo…
- [SentientNr6/claude-mods](https://github.com/SentientNr6/claude-mods) - A collection of plugins for Claude.
- [shahsanket2107/clarvis](https://github.com/shahsanket2107/clarvis) - Clarvis: um mod de fã não oficial dos Avengers para o Claude Code.
- [shengyy/ccoverhead](https://github.com/shengyy/ccoverhead) - Mod de Claude Code para contexto, crescimento, cota, cache, custo nativo e…
- [shezis/claude-model-router](https://github.com/shezis/claude-model-router) - Mod de código do Claude: encaminha turnos simples e subagentes para modelos…
- [shissncg/claude-mods](https://github.com/shissncg/claude-mods)
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [Spendry/claude-code-mods](https://github.com/Spendry/claude-code-mods) - Claude Code mods, installable as a plugin marketplace: deviation-kernel guards…
- [speti4/doom-pane](https://github.com/speti4/doom-pane) - O DOOM original em um painel do Claude Code, sem nada para instalar: o…
- [StalicJi/my-mods](https://github.com/StalicJi/my-mods) - 個人 Claude Code mod…
- [SteveAnthonyFM/subagent-guard](https://github.com/SteveAnthonyFM/subagent-guard) - Keep Claude.
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensagens de commit com um clique para Claude Code com uma Malenia dançante em…
- [Sunkanxx/Mods](https://github.com/Sunkanxx/Mods) - Claude Code mods — marketplace sunkanxx-mods.
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — uma modificação do Claude Code que mostra o uso do seu plano…
- [tartinerlabs/claude-code-mods](https://github.com/tartinerlabs/claude-code-mods)
- [thangdo19/claude-code-mods](https://github.com/thangdo19/claude-code-mods) - Pequenos mods que mudam a aparência e os sons do Claude Code.
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Um mod do Claude Code que mostra a sessão atual em um painel: cada prompt, o…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Um marketplace de plugins do Claude Code de mods: plugins function-hooks que…
- [thinhkhuat/prompt-enhancer](https://github.com/thinhkhuat/prompt-enhancer) - Mod do Claude Code: reescreve um prompt rudimentar no próprio lugar, nomeando…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Ouça as respostas do Claude Code enquanto a frase lida é destacada.
- [tunglt1810/claude-gadgets](https://github.com/tunglt1810/claude-gadgets) - Some Claude mods.
- [twentynineteen/scrooge-context-vault](https://github.com/twentynineteen/scrooge-context-vault) - Claude Code mod: your context window as Scrooge McDuck.
- [tyree88/tempered_plugins](https://github.com/tyree88/tempered_plugins) - Claude Code mods from Tempered Works: ship-state, timeline, limit-resume — plus…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod do Claude Code: cota de 5h/7d, janela de contexto, tempo restante do cache…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod do Claude Code: faixa de progresso animada e resumo de conclusão para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Três pequenos mods de Claude Code: veja quando seus subagentes terminarão…
- [varunmoka7/image-shrinker](https://github.com/varunmoka7/image-shrinker) - Reduz o tamanho de capturas de tela grandes antes que Claude as leia, para que…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Diga &quot;Estou perdido&quot; e Claude explicará novamente sua última resposta em…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Exibe os próximos prompts sugeridos acima da caixa de prompt.
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Faça uma pergunta paralela a Claude em um painel ao lado do seu trabalho.
- [vihrea1337/pager](https://github.com/vihrea1337/pager) - Claude Code pings you in Telegram when a task is done or it waits for…
- [WeaponizedLego/claude-code-mods](https://github.com/WeaponizedLego/claude-code-mods) - Meus mods do Claude Code.
- [wimcraft/godville-pane](https://github.com/wimcraft/godville-pane) - A Claude Code mod: your Godville hero and diary in a sidebar.
- [wnsogabriel/claude-mods](https://github.com/wnsogabriel/claude-mods) - Mods para o Claude Code: faixa de limites de uso (5h/semanal) e painel de…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin do Claude Code: seus limites de uso do Claude Pro/Max com previsão de…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para o Claude Code. agent-crew: acompanhe seus subagentes trabalhando como…
- [yeonwooook/claude-study-latex](https://github.com/yeonwooook/claude-study-latex) - Exiba matemática em LaTeX em linha e em bloco, além de figuras TikZ opcionais…
- [YohanGarcia/agent-taskboard](https://github.com/YohanGarcia/agent-taskboard) - Um quadro de tarefas ao vivo para o Claude Code: planeje antes de criar…
- [zaripovfarrukh/claude-code-mods](https://github.com/zaripovfarrukh/claude-code-mods)
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Uma coleção selecionada a dedo dos melhores recursos para os agentes mais…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Um plugin do Claude Code que mostra o que está acontecendo — uso de contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Linha de status bonita e altamente personalizável para Claude Code CLI, com…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas as partes do prompt de sistema do Claude Code, 27 descrições de…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code &amp; Codex — cinematic product videos with…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mais de 45 dicas para aproveitar ao máximo o Claude Code, do básico ao avançado…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / Codex skill — gere carrosséis do Xiaohongshu e pares de capas…
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Powerline elegante no estilo vim para o Claude Code.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revise o diff do seu agente de programação em um painel do terminal e envie…
- [devswha/herdr-web-ui](https://github.com/devswha/herdr-web-ui) - Browser and phone client for herdr: chat and live terminal for every agent…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin abrangente de linha de status para o Claude Code, com uso de contexto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crie mods para Claude Code: conecte qualquer solicitação, modifique qualquer…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Um painel completo de status para Claude Code — informações da sessão, barras…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: acompanhe a pegada de carbono das suas sessões do Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Uma linha de status estética para Claude Code, criada por awesomejun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - Agente de roleplay de histórias longas para DeepSeek Harness.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mods públicos para Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash e guias para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs legais e gratuitos + agentes de programação — atualização…
- [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) - DeepSeek Harness Tavern Plugin - character card roleplay, worldbook management…
- [backstabslash/goccc](https://github.com/backstabslash/goccc) - Calculadora de custos rápida, sem dependências, e statusline personalizável…
- [kylesnowschwartz/tail-claude-hud](https://github.com/kylesnowschwartz/tail-claude-hud) - Linha de status do terminal para sessões do Claude Code.
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Placar ao vivo de futebol, jogos e classificações da competição que você…
- [WormAlien/hub-cc](https://github.com/WormAlien/hub-cc) - Plano de controle local para Claude Code em Windows e macOS: alterne gateways…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill que transforma seu agente de programação em especialista em…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horários de oração, data Hijri, adhkar, ayah diária, jejum sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuração pessoal do Claude Code versionada dentro de ~/.claude — agentes…
- [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) - Suíte de geração de imagens e processamento visual para DeepSeek Harness…
- [GoSlowPoke168/claude-statusline](https://github.com/GoSlowPoke168/claude-statusline) - Statusline truecolor de duas linhas para Claude Code.
- [proDreams/dsh-tidewatch](https://github.com/proDreams/dsh-tidewatch) - Um cartão flutuante de maré de pico/fora de pico para DeepSeek Harness: i18n…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Coleção de plugins para Claude Code, pi e DeepSeek Harness: HUD da barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de ferramentas portátil do Claude Code para .NET DDD/Clean Architecture…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuração global portátil do Claude Code: skills personalizadas, hooks…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins do Claude Code que uso todos os dias: skills e mods, organizados para…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods não oficiais para a aba Code do Claude Desktop — usage-pet: uma faixa de…
- [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) - DSH &lt;-&gt; Feishu (Lark) bridge, self-developed (not a fork): streaming reply card…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins e skills do Claude Code para facilitar mods do jogo…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Governança de tokens para Claude Code: o modelo principal direciona, e a…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Statusline ao vivo da fase do fluxo de trabalho para o Claude Code.
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositório de mods Awesome Media para Claude Code.
- [tedserbinski/claude-code-statusline](https://github.com/tedserbinski/claude-code-statusline) - Configuração simples e útil de statusline para Claude Code.
- [cesarschutz/claude-code-kit](https://github.com/cesarschutz/claude-code-kit) - Marketplace de plugins para o Claude Code: mods, skills, agentes, hooks…
- [crosscountryridinggirlwonder916/claude-statusline](https://github.com/crosscountryridinggirlwonder916/claude-statusline) - Exibe a statusline do Claude Code com limites de taxa, diretório atual e…
- [eddundead/claude-poker](https://github.com/eddundead/claude-poker) - 8-bit Texas Hold.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Linha de status configurável do Claude Code para Linux, WSL, Windows e macOS…
- [JairoTorregrosa/claude-statusline](https://github.com/JairoTorregrosa/claude-statusline) - Linha de status rápida do Rust para o Claude Code — prioriza o payload, git em…
- [jsh135790/claude-code-capsule-panel](https://github.com/jsh135790/claude-code-capsule-panel) - Um painel de uso ao vivo para o Claude Code — detalhamento do contexto, acertos…
- [jv-k/claude-gauge](https://github.com/jv-k/claude-gauge) - Uma linha de status e uma linha de tokens para Claude Code: contexto, uso de 5…
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Exiba detalhes-chave de status para Claude Code, incluindo modelo, contexto…
- [Obednal97/claude-statusline-kit](https://github.com/Obednal97/claude-statusline-kit) - Linha de status do Claude Code com várias linhas: gasto, % de contexto, git e…
- [salvanya/claude_code_statusline](https://github.com/salvanya/claude_code_statusline) - Statusline com informações úteis para claude code.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipes de agentes nativas. Sob controle.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Complementos do Claude Code: monitor de ponto colorido do status das abas +…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Fábricas de software definíveis para o Claude Code no herdr: grafos de estações…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Linha de status de uso do Claude Code para macOS e Linux, empacotada como um…
- [alfredwesterveld/claude-cache-status](https://github.com/alfredwesterveld/claude-cache-status) - Claude Code desktop mod: prompt-cache TTL countdown, hit rate and misses.
- [andkirby/claude-statusline](https://github.com/andkirby/claude-statusline) - Linha de status personalizada para o Claude Code — barra de contexto com…
- [AsyrafHussin/claude-code-statusline](https://github.com/AsyrafHussin/claude-code-statusline) - Uma linha de status limpa e informativa para o Claude Code — mostra projeto…
- [aubinhaba/claude-code-payment-skills](https://github.com/aubinhaba/claude-code-payment-skills) - Claude Code plugin: code-review skills for payments, consistency, boundaries…
- [BedirYilmaz/claude-crt-hud-mod](https://github.com/BedirYilmaz/claude-crt-hud-mod) - Modificação CRT HUD do Claude: um painel de status no estilo CRT para o Claude…
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Marketplace de plugins do Claude Code com baloo: habilidades, um agente que…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Claude Code status line in Lua, with a live Neovim playground.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Linha de status profissional do Claude Code: duração da sessão, custo em várias…
- [cvrt-gmbh/claude-statusline](https://github.com/cvrt-gmbh/claude-statusline) - Linha de status do Claude Code ciente da assinatura.
- [diegorv/koko.claude-statusline](https://github.com/diegorv/koko.claude-statusline) - Uma linha de status rica para o terminal do Claude Code — Bun + TypeScript, sem…
- [fbandres/ccmods](https://github.com/fbandres/ccmods) - Mods for Claude Code: live panes, gauges and more, installable as plugins.
- [filtercoffeeway/claude-kit](https://github.com/filtercoffeeway/claude-kit) - Ferramentas, habilidades e agentes para o Claude Code — começando com uma linha…
- [giribboy77-arch/claude-statusline](https://github.com/giribboy77-arch/claude-statusline) - Statusline personalizada do Claude Code.
- [hardtomakeanadress/claude-code-deepseek-cost](https://github.com/hardtomakeanadress/claude-code-deepseek-cost) - Gasto real do DeepSeek com API para o Claude Code: recalcula os preços das…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Visualize imagens dentro do Claude Code: passe o cursor sobre um chip abaixo de…
- [irfanfaraaz/claude-kit](https://github.com/irfanfaraaz/claude-kit) - My Claude Code setup: mods, skills and plugins.
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincronize as tarefas do Claude com o Fizzy.do para obter visibilidade da…
- [kernastra/claudecode](https://github.com/kernastra/claudecode) - A collection of Claude Code skills, mods, and other add ons that I.
- [Leechlike-intangibleasset343/claude-code-statusline](https://github.com/Leechlike-intangibleasset343/claude-code-statusline) - Acompanhe o status do Claude Code com um painel compacto que mostra contexto…
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Instalador de ambiente do Claude Code: skills, statusline, hooks, permissões e…
- [muemadennis/claude-code-command-center](https://github.com/muemadennis/claude-code-command-center) - Claude Code Live Dashboard 2026: Track Costs, Tokens &amp; Git Branch Status.
- [OpenClawFarm/claude-statusline](https://github.com/OpenClawFarm/claude-statusline) - Linha de status no estilo HUD para o Claude Code — saúde da rede, TPS…
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — Claude Code statusline for macOS + Linux.
- [rotemx-10x/claude-code-statusline](https://github.com/rotemx-10x/claude-code-statusline) - A two-line status line for Claude Code.
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuração portátil do Claude Code (statusline + instalador).
- [SohamShirsat/claude-cockpit](https://github.com/SohamShirsat/claude-cockpit) - Um pequeno painel para o Claude Code: porcentagem de contexto, contagem…
- [speti4/claude-statusline](https://github.com/speti4/claude-statusline) - Barra de status personalizada do terminal para o Claude Code: modelo…
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuração portátil do Claude Code: CLAUDE.md, configurações, linha de…
- [Tina0529/claude-session-radar](https://github.com/Tina0529/claude-session-radar) - Mod do Claude Code para desktop (macOS): notificações de sessão com clique para…
- [vibe-coding-labs/claude-code-status-skills](https://github.com/vibe-coding-labs/claude-code-status-skills) - Claude Code status line: the current model ID, the hostname, a clickable git…
- [vladimir-ks/ai-agile-claude-code-statusline](https://github.com/vladimir-ks/ai-agile-claude-code-statusline) - Acompanhamento de custos em tempo real e linha de status de monitoramento de…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Skill do Claude Code (VS Code, Windows): prévias de imagens e botões de…
- [ymoud/claude-code-statusline](https://github.com/ymoud/claude-code-statusline) - Uma linha de status do Claude Code: pasta, branch do git, modelo, uso da janela…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de deterioração de contexto 2026 — Monitor proativo de memória de IA e…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes e linhas de status do Claude Code: coleções e ferramentas de…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Um construtor visual de statuslines para o Claude Code.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline do Claude Code mostrando o uso de tokens em tempo real e o consumo…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: painéis, faixas e companheiros baseados em hooks de…
- [timvdhoorn/cc-my-pi](https://github.com/timvdhoorn/cc-my-pi) - Claude Code-style UI bundle for the Pi coding agent — tool rendering, spinner…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passe tarefas entre suas sessões do Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Isto em um servidor MCP para controlar o MODS, a ferramenta modular…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex e Claude Code para traduzir mods de CK3 com um LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código aberto e outras extensões para Claude Code.
- [Apparux/cc-fusion](https://github.com/Apparux/cc-fusion) - Linha de status do Claude Code: beleza do CCometixLine + funcionalidade de HUD…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encontre o que você pede ao Claude Code repetidamente e transforme…
- [Niedvin/ClauDiscobombulating](https://github.com/Niedvin/ClauDiscobombulating) - Mod prompt-bar para Claude Code: limites de uso, temporizador e alerta do…

</details>

<a id="dsh-cordis"></a>

## Ecossistemas de plugins do DSH e do Cordis

DeepSeek Harness e Cordis chegam ao mesmo lugar por uma direção diferente: para eles, o plugin é o mecanismo de modificação; portanto, um plugin lá equivale a um mod aqui.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74351 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

🌊 O agent harness original. Implante enxames inteligentes multiagente, coordene fluxos de trabalho autônomos e crie sistemas de IA conversacional. Inclui memória adaptativa, inteligência de autoaprendizado, federação, integração com RAG vetorial e integração nativa com Claude Code / Codex / Hermes e muitos outros

<sub>🔧 Encontrado em uso no código: `plugins/ruflo-swarm/README.md`, `plugins/ruflo-swarm/hooks/model/members.ts`, `v3/docs/validation/mod-api-coverage-2026-10.md`, `plugins/ruflo-swarm/hooks/register.ts`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                          |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **74351**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100550 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🎨 Melhor plugin de design para DeepSeek Harness. A alternativa de código aberto ao Claude Design. 🖥️ Aplicativo desktop local-first. 🖼️ Seu agente de programação se torna o mecanismo de design: protótipos, landing pages, dashboards, slides, imagens e vídeos — arquivos reais, exportação para HTML/PDF/PPTX/MP4. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode e mais de 20 CLIs via BYOK.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **100550** |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐97943 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Faça engenharia reversa de qualquer coisa com agentes, desde o comportamento de aplicativos até binários nativos.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **97943**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82003 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Transforme qualquer ideia, plano ou base de código em um belo diagrama interativo. Uma habilidade de agente para Claude Code, Codex e muito mais.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **82003**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35766 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Um agente de programação confiável para tarefas complexas de engenharia de software.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Go                                                                                     |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **35766**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25500 · Python · 🔎 inferred · 19 天</summary>

##### 📝 Summary

Distilly — transforme a forma como eles pensam em Skills reutilizáveis para qualquer Agent ou Bot. Anteriormente Colleague Skill（原同事 Skill）.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25500**  |
| Last push    | 2026-09-22 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/bf54e387044cab88.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18396 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Uma lista selecionada de plugins para DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18396**  |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget">MeteorNOX/DeepSeek-Balance-Whale-Widget</a></b> · ⭐4492 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness（DSH）uma garota-baleia que vive no canto inferior direito da interface do DSH e ajuda você a acompanhar o saldo da conta DeepSeek. Fofa e elástica, oferece suporte a arrastar e encaixar, virar ao encaixar à esquerda e animação de rolagem numérica; é ativada automaticamente com a interface. Recomenda-se chamar diretamente sua instalação do dsh

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4492**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `dsh-plugins` · `floating-widget`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/meteornox--deepseek-balance-whale-widget/c17efbb95a7522ee.png" width="100%" alt="MeteorNOX/DeepSeek-Balance-Whale-Widget screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4292 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

O plugin TUI oficialmente mais recomendado pelo DSH — alto desempenho, baixo overhead, baleia pixelada fofa e interação fluida com o mouse. Instalação com um comando via npm. / O plugin TUI oficialmente mais recomendado pelo DSH: alto desempenho, baixo consumo, baleia pixelada fofa, interação fluida com o mouse e instalação com um comando via npm

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4292**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/omdsh-dev/DSH-better-sidebar">omdsh-dev/DSH-better-sidebar</a></b> · ⭐4112 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Base aberta para barra lateral, com suporte a extensões de terceiros que registram novas páginas na barra lateral. Inclui renderização/edição de arquivos, terminal, conversa lateral, Git e páginas de subagentes.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4112**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `sidebar`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/0f9147e51f645f82.png" width="100%" alt="omdsh-dev/DSH-better-sidebar screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/omdsh-dev--dsh-better-sidebar/db34cbdf93687219.gif" width="100%" alt="omdsh-dev/DSH-better-sidebar animation"><br><sub>gravação animada · <a href="https://github.com/user-attachments/assets/23187822-047e-45cc-b480-fe997bd55b86">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3682 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The World's First Virtual Terminal for AI Agents

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3682**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3092 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Tauri versão desktop | Instalador de apenas 8mb, configuração de ambiente zero, plugins predefinidos, Windows / macOS / Linux.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3092**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐1995 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板及浏览器和侧边栏与 Context 命令，透视上下文组成、演进、压缩、剪枝等事件与动作。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1995**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1837 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

通过扫码或机器人凭据把IM机器人接入DeepSeek Harness（支持飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord和WhatsApp）。 Connect IM bots to DeepSeek Harness via QR code or credentials (9 channels).

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1837**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/Agents-Anywhere">anywhere-labs/Agents-Anywhere</a></b> · ⭐1577 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

跨设备的开源Agent工作台

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1577**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `acp` · `agentclientprotocol` · `agents` · `claudecode` · `codex` · `codex-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/anywhere-labs/Agents-Anywhere/main/docs/images/readme-hero-zh.webp" width="100%" alt="anywhere-labs/Agents-Anywhere screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/EthanYoQ/AI-Novel-Writer">EthanYoQ/AI-Novel-Writer</a></b> · ⭐1410 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Software de criação de romances com AI: organiza inspiração, personagens, construção de mundo, esboços, escrita de capítulos, revisão e edição em um fluxo controlável; oferece versões desktop para Windows/macOS, com suporte a modelos locais e online. Software de escrita de romances com AI: organiza inspirações, personagens, construção de mundo, esboços, redação de capítulos, revisão e edição em um fluxo de trabalho controlável. Oferece aplicativos desktop para Windows/macOS, integração com Ollama e uma prévia do plugin DeepSeek Harness (DSH).

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1410**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-writing` · `creative-writing` · `deepseek-harness` · `dsh-plugin` · `electron` · `fiction-writing` · `local-first` · `long-form-fiction`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ethanyoq--ai-novel-writer/97081b4a6febc6aa.png" width="100%" alt="EthanYoQ/AI-Novel-Writer screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1172 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Memória para Claude Code, Codex, Cursor e mais 38 agentes de código, criada a partir do histórico de sessões já armazenado no seu disco. Busca local, MCP e hooks, sem LLM, um único binário Go.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Go                                                                                     |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1172**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/agentrq/agentrq">agentrq/agentrq</a></b> · ⭐1140 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

AgentRQ: Human-in-loop realtime conversational task manager for AI Agents. Self-hosted! Control your own agents from wherever you want Mobile, Web, Desktop. Designed to work well with your own Claude subscriptions and any harness with ACP support.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Go                                                                                     |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1140**   |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `acp-client` · `acp-gateway` · `agentic-ai` · `agentic-workflow` · `agents` · `ai-memory` · `claude-code` · `claude-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/71791429350e448f.png" width="100%" alt="agentrq/agentrq screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/agentrq--agentrq/e4115ab2a9de3317.gif" width="100%" alt="agentrq/agentrq animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/myYangyunfan/dsh_desktop">myYangyunfan/dsh_desktop</a></b> · ⭐705 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Cliente desktop do DeepSeek Harness (dsh) Windows — Node.js + dsh CLI integrados, inicialização com um clique

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **705**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `desktop` · `desktop-app` · `dsh` · `dsh-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/myyangyunfan--dsh_desktop/822cff4e94634530.png" width="100%" alt="myYangyunfan/dsh_desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vibeinging/dsh-desktop">vibeinging/dsh-desktop</a></b> · ⭐592 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **592**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `agentic-workflows` · `ai-agent` · `ai-workbench` · `data-analysis` · `deepseek-harness` · `desktop-app` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vibeinging--dsh-desktop/ccbf15d3a2c42437.png" width="100%" alt="vibeinging/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/d-dev0101/open-sea-skin">d-dev0101/open-sea-skin</a></b> · ⭐389 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🌊 DeepSeek Harness 海洋皮肤与动态主题 | Real-time ocean theme with adjustable waves, sunset & glass opacity. DSH plugin + Chrome/Edge extension; keeps your new-tab homepage.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **389**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `animated-background` · `chrome-extension` · `customization` · `deepseek` · `deepseek-harness` · `deepseek-theme` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/3d9689f0d936d1b0.png" width="100%" alt="d-dev0101/open-sea-skin screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/d-dev0101--open-sea-skin/ccd6ac3920478ffa.gif" width="100%" alt="d-dev0101/open-sea-skin animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/DDDMUC/dsh-free-search">DDDMUC/dsh-free-search</a></b> · ⭐369 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **369**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `bing` · `deepseek-harness` · `dsh` · `dsh-plugin` · `duckduckgo` · `web-search`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dddmuc--dsh-free-search/ec034e713544ead5.png" width="100%" alt="DDDMUC/dsh-free-search screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐255 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

ACRYL - Agent Context Relay Yielding Lifecycles. Um espaço de trabalho persistente, um contexto canônico, qualquer agente de codificação.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **255**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐225 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏与随机，纯原生 token 系统实现。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **225**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐203 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin nativo do DeepSeek Harness (DSH) que integra TypeSafe Jev ou uma API de decisão como luna como uma camada de decisão System One para seleção, supervisão, correções e aprovações de agentes.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **203**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cocofhu/anime-find">cocofhu/anime-find</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **176**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `anime` · `anime-search` · `bangumi` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `magnet`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cocofhu--anime-find/4e8000425bf8bf5f.jpg" width="100%" alt="cocofhu/anime-find screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐176 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **176**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KelaoHu/dsh-lowtide">KelaoHu/dsh-lowtide</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Delegação de tarefas com mudança de horário para DeepSeek Harness (dsh): planeje tarefas quando quiser, elas serão executadas sem supervisão fora do horário de pico e você poderá voltar para consultar um relatório. Avaliação feita por humanos, desktop + web.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **172**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `ai-agent` · `automation` · `batch-processing` · `cordis` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kelaohu--dsh-lowtide/3d2509a82d1a3f11.png" width="100%" alt="KelaoHu/dsh-lowtide screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐165 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin do DeepSeek Harness para migração de sessões entre predefinições com visualização prévia. Transferências com esquema fixo preservam o estado, a intenção do modelo de origem e as imagens não resolvidas; a sessão original permanece inalterada.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **165**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐160 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH): GPT-6 & Codex models, images, web search and quota via ChatGPT sign-in — no OpenAI API key. Beta: control DSH from the ChatGPT mobile app. 在 DSH 中使用 ChatGPT 订阅，并可用 ChatGPT 手机 App 远程控制。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **160**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/0c3daa4061aa684e.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/flameox">morluto/flameox</a></b> · ⭐142 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Evidências de runtime que ajudam agentes a rastrear, criar perfis e eliminar hotspots em código de aplicação e nativo, kernels GPU e stacks de inferência.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **142**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `benchmarking` · `coding-agents` · `cordis` · `debugging` · `developer-tools` · `dsh` · `dsh-plugin` · `gpu-profiling`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--flameox/2914b7977590380e.png" width="100%" alt="morluto/flameox screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/FeatherHunter/dsh-mattpocock-skills-deck">FeatherHunter/dsh-mattpocock-skills-deck</a></b> · ⭐134 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

安装即自带mattpocock/skills v1.3.1的27个工程与效率技能，无需手动装技能。400亿token打造本插件，在原始技能之上提供10倍的开发效率，也能帮助新手更快上手该技能套件。全力支持GitHub issue；Markdown为预览版；GitLab暂不支持。感谢您的使用和支持💗

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **134**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `agent` · `ai` · `claude` · `deepseek-harness` · `dsh` · `dsh-better-sidebar` · `dsh-plugin` · `github-issues`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/featherhunter--dsh-mattpocock-skills-deck/c4bd78003446c161.png" width="100%" alt="FeatherHunter/dsh-mattpocock-skills-deck screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐133 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Tema desktop do Claude Code para o DeepSeek Harness｜ Tema desktop do Claude Code criado para a GUI Web do DeepSeek Harness

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **133**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-10 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WestFox-AwA/dsh-prompt-optimizer">WestFox-AwA/dsh-prompt-optimizer</a></b> · ⭐113 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin DSH · otimizador por injeção 0.8 (linha principal): você fala normalmente, e ele esclarece "o que exatamente é necessário nesta rodada" depois que você envia e antes de a IA receber, então entrega esse entendimento à IA de trabalho (injeção de contexto) — sem reescrever as palavras originais, com base literal para cada item. Inclui interface de controle (nível/permissões/modelo/contexto/ferramentas somente leitura), camada flutuante de interceptação (camada de pensamento + camada de saída) e uso real de tokens. Pode melhorar claramente a estabilidade de desempenho da maioria dos modelos, especialmente DeepSeek-V4.1-Flash, com melhora evidente

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **113**    |
| Last push    | 2026-10-11 |
| First listed | 2026-10-11 |

🏷 `agent-workflow` · `ai-agent` · `cordis` · `deepseek` · `dsh` · `dsh-plugin` · `llm` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/westfox-awa--dsh-prompt-optimizer/3098cfd264cf8ca0.png" width="100%" alt="WestFox-AwA/dsh-prompt-optimizer screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 72</sub></summary>

- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Uma proteção pré-execução para agentes de programação com IA.
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Uma lista selecionada dos melhores plugins incríveis de IA para assistentes de…
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) - 30 秒找到真正适合你的 DeepSeek Harness插件。每天自动抓取 GitHub 上的 `dsh-plugin`…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin DSH — modelos OpenCode Zen gratuitos para DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins DSH / DSH Plugin Marketplace: navegue, instale e atualize…
- [arcships/rutis](https://github.com/arcships/rutis) - Um runtime de plugins para softwares que iteram sobre si mesmos — a base onde…
- [EricWang1358/dsh-web-studyhub](https://github.com/EricWang1358/dsh-web-studyhub) - StudyHub: a DeepSeek Harness (DSH) plugin that turns your own material into…
- [kukucaiCndy/Corum-Harness](https://github.com/kukucaiCndy/Corum-Harness) - Versão desktop do Agent criada com base no núcleo do Deepseek-Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - O diretório vivo de plugins do DeepSeek Harness — atualizado a cada hora…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - Recuperação de contexto do espaço de trabalho e rastreamento do ciclo de vida…
- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) - sofagent is an open-source FDE Harness for AI coding agents — on entry, write…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Diretório selecionado de plugins do DeepSeek Harness (DSH) — mais de 280…
- [GZX2211/dsh-Visual-Workflow](https://github.com/GZX2211/dsh-Visual-Workflow) - 可视化 Agent 编排平台｜基于 DeepSeek Harness，支持 Workflow、Multi-Agent、元编排、MCP 与…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - Plugin mestre de recursos para jogos do dsh.
- [HOWILLMAKEIT/dsh-model-context-catalog](https://github.com/HOWILLMAKEIT/dsh-model-context-catalog) - DeepSeek Harness 插件：一键匹配模型上下文窗口，展示容量来源，支持勾选批量配置、已有窗口管理和手动编辑.
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT：sistema de agentes para chats em grupo multiplataforma baseado no…
- [wingsky-1/dsh-plugin-hub](https://github.com/wingsky-1/dsh-plugin-hub) - Coleção de plugins de GUI web DSH (DeepSeek Harness) — notificações de tarefas…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, ferramentas, skills e recursos de aprendizagem do DeepSeek Harness…
- [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) - Plugin gerenciador de servidores MCP para DeepSeek Harness: página…
- [BotHarness/DeepSeekBot](https://github.com/BotHarness/DeepSeekBot) - Open-source GrokBot alternative built on DeepSeek Harness.
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociação comercial A2A + plugin DeepSeek Harness (dsh).
- [Imzl-zl/dsh-toolbox-ui](https://github.com/Imzl-zl/dsh-toolbox-ui) - Painel de ferramentas para o DeepSeek Harness Web: gerenciador de MCP…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin do DeepSeek Harness · botão «otimizar» com um clique na barra de envio…
- [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) - Verified plugin marketplace and autonomous registry for DeepSeek Harness.
- [liustack/pptwise](https://github.com/liustack/pptwise) - Um PowerPoint de verdade, não HTML. Diga à sua IA o que abordar e o pptwise…
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Grafo de conhecimento de código com prioridade local e harness de contexto para…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles…
- [AmethystLuna/embedded-workbench](https://github.com/AmethystLuna/embedded-workbench) - Plugin de engenharia de IA para C/C++ embarcado — skills de firmware.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - Transforme os modelos já conectados no aplicativo de desktop local WorkBuddy…
- [MichaelShii/dsh-plugin-teamflow](https://github.com/MichaelShii/dsh-plugin-teamflow) - plugin dsh teamflow.
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Testes contínuos de compatibilidade para plugins do DeepSeek Harness: versões…
- [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) - Compactação agressiva de contexto para agentes local-first.
- [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) - Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429…
- [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) - Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes…
- [GooDAnDReaDY/dsh-voice](https://github.com/GooDAnDReaDY/dsh-voice) - Voice input for DeepSeek Harness: dictation and voice messages with…
- [vecnode/vncode](https://github.com/vecnode/vncode) - vncode 🤖 Agent-Human IDE ⌨️ Web and Desktop versions, bundles Plugins, Skills…
- [bonerush/dsh-obsidian-mem](https://github.com/bonerush/dsh-obsidian-mem) - DeepSeek Harness host plugin that keeps project documents and long-term memory…
- [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) - A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified…
- [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) - Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH).
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Raio-X dos plugins do DeepSeek Harness: capacidades declaradas versus…
- [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) - DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）.
- [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) - Mobile gateway and secure local network access for DeepSeek Harness WebUI.
- [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) - Session deep links + full session export (markdown/JSON) + approved…
- [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) - Mixture of Agents (MoA) plugin for DeepSeek Harness with /moa slash command…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) - MUV Variable Table Editor - tavern companion plugin for DeepSeek Harness…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace com várias pastas: permite que o Agent do DSH (DeepSeek Harness) leia…
- [GooDAnDReaDY/dsh-gitea](https://github.com/GooDAnDReaDY/dsh-gitea) - Gitea/Forgejo toolkit for DeepSeek Harness: issues, PRs, CI, releases…
- [jinhuang712/dsh-survey](https://github.com/jinhuang712/dsh-survey) - Questionnaire-style batch questioning plugin for DeepSeek Harness: 10+…
- [majiayu000/dsh-plugin-registry](https://github.com/majiayu000/dsh-plugin-registry) - Searchable DeepSeek Harness plugin registry with curated listings and…
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Padrão de verificação sem dependências para plugins do DeepSeek Harness (dsh)…
- [Retr67/dsh-opencode-models](https://github.com/Retr67/dsh-opencode-models) - Plugin do DeepSeek Harness (DSH): sincronização do modelo OpenCode Go em um…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode no DeepSeek Harness — plugin DSH que mantém OpenCode Zen + modelos de…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins de terceiros e gerenciador protegido do…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx é uma estação de trabalho desktop expansível e centrada nas pessoas…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Um agente de codificação completo para o DeepSeek Harness — fluxos de trabalho…
- [GooDAnDReaDY/dsh-tts](https://github.com/GooDAnDReaDY/dsh-tts) - Natural speech synthesis plugin for DeepSeek Harness.
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - Dê ao DeepSeek Harness Agent mãos e pés nativos para operar GitHub! Reutiliza…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — conjunto de ferramentas comunitário de implantação e operações…
- [Seelerc/dsh-plugin-delete-archived](https://github.com/Seelerc/dsh-plugin-delete-archived) - Permanently delete archived DeepSeek Harness sessions along with their on-disk…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web do DeepSeek Harness (DSH): aba lateral market-dashboard para…
- [tiphareth0/dsh-hardssh](https://github.com/tiphareth0/dsh-hardssh) - Run your work with existing DSH plugins on remote servers, across any number of…
- [argszero/cordis-plugin-empty-response-retry](https://github.com/argszero/cordis-plugin-empty-response-retry) - Torna uma tentativa vazia de modelo sem atribuição passível de nova tentativa…
- [argszero/cordis-plugin-goal-progress-guard](https://github.com/argszero/cordis-plugin-goal-progress-guard) - Progress judgement for dsh autonomous goal rounds: defer the loop while…
- [eovidiu/cordis-ios](https://github.com/eovidiu/cordis-ios) - Plugins que fazem a própria limpeza: uma adaptação do framework de plugins…
- [Magica-Chen/dsh-preset-codex-claude](https://github.com/Magica-Chen/dsh-preset-codex-claude) - Predefinição de agente DeepSeek Harness: Codex e Claude Code como subagentes de…
- [validation-engineering/cordis-verus](https://github.com/validation-engineering/cordis-verus) - Um runtime de plugin Rust com um kernel de ciclo de vida verificado por Verus e…
- [YOU-SHOULD-KNOW-ME/antigrative-dashboard](https://github.com/YOU-SHOULD-KNOW-ME/antigrative-dashboard) - Inline Antigravity dashboard: tok/s, DSH-style cache hit rate, five-hour and…
- [Jecvay/paseo-dsh-direct](https://github.com/Jecvay/paseo-dsh-direct) - DeepSeek Harness 的 Paseo Provider Plugin (Direct Provider).
- [SCP-008-1/dshop](https://github.com/SCP-008-1/dshop) - dsh 插件商城 - 基于 GitHub topic:dsh-plugin 自动发现与每小时定时同步.

</details>

<a id="writing"></a>

## Textos, discussões e vídeos

Textos, discussões e vídeos sobre a capacidade de mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 10 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 3 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-09 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 3 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-08 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 10 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

##### 📝 Summary

Olá, HN, criei isto para mim e quis disponibilizá-lo como código aberto. O problema: eu queria uma forma de receber lembretes entre prompts, pois costumo passar muitas horas no terminal, especialmente agora que geralmente processamos tantos agentes em paralelo. A primeira versão era um rep simples

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-06 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 2 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-10 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 8 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Summary

No upstream description was published.

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 9 天</summary>

##### 📝 Summary

Criei isto porque, com os modelos de codificação mais recentes, Claude entra em modo de trabalho profundo com comandos obscuros, e eu já não sei o que ele está fazendo. Este é um mod (um plugin que usa os novos hooks de função do Claude Code) que desenha uma linha acima do prompt: - a etapa atual,

##### 📌 Basic facts

| Field    | Value                                                                 |
| -------- | --------------------------------------------------------------------- |
| Category | `Textos, discussões e vídeos`                                         |
| Evidence | `o próprio texto menciona um mod API ou declara a capacidade de mods` |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| First listed | 2026-10-05 |

</details>

<a id="projects-by-implementation-language"></a>

## Projetos por linguagem de implementação

O ecossistema está concentrado em Python e TypeScript, mas clientes tipados continuam surgindo em outras linguagens. Esta tabela é gerada a partir das próprias entradas.

| Linguagem  | Entradas | Exemplos                                                                                                      |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| TypeScript | 382      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 96       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 35       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 23       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15       | `awss1i/assay`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                            |
| Go         | 6        | `backstabslash/goccc`, `kylesnowschwartz/tail-claude-hud`, `bunderlog/claude-plugins`                         |
| Rust       | 6        | `persiyanov/herdr-reviewr`, `JairoTorregrosa/claude-statusline`, `OpenClawFarm/claude-statusline`             |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                       |
| Lua        | 1        | `crafts69guy/claude-statusline.nvim`                                                                          |
| PowerShell | 1        | `GoSlowPoke168/claude-statusline`                                                                             |
| Swift      | 1        | `eovidiu/cordis-ios`                                                                                          |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Correções são bem-vindas e são a maneira mais rápida de melhorar esta lista. Abra uma issue ou um pull request se uma entrada estiver na categoria errada, com a classificação errada ou se um projeto tiver sido excluído indevidamente por colisão de nome — essa é a categoria em que filtros automatizados têm maior probabilidade de errar.

---

<sub>Projeto independente da comunidade. Não afiliado, endossado nem revisado por Anthropic. Claude Code, Claude e Anthropic são marcas registradas de Anthropic. O comportamento do produto pode mudar sem aviso; verifique tudo o que for essencial na documentação oficial. Os ativos permanecem propriedade de seus projetos de origem e são reproduzidos somente quando uma licença permite.</sub>

<sub>Last updated · 2026-10-12T03:53:55+08:00</sub>
