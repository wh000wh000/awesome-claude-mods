<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods incríveis do Claude">
</p>

<h1 align="center">Mods incríveis do Claude</h1>

<p align="center"><b>O índice de mods e plugins do Claude Code classificados por evidências, além dos comportamentos mais profundos que eles alteram.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-494-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Português</b> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice ativo** · Última sincronização: `2026-10-13T21:42:20+08:00` (UTC+8)
> · Entradas: **494** · Adicionadas na atualização mais recente: **0** · Linguagens de implementação: **13**

<sub>Cada entrada abaixo foi coletada, filtrada e verificada novamente de forma automática. Nada aqui é uma inserção paga.</sub>

<a id="featured"></a>

## Destaques do momento

<sub>Uma entrada por categoria, classificada pelo grau de evidência e pelo número de estrelas, recalculada a cada atualização. É uma classificação, não uma recomendação; cada destaque leva ao respectivo card completo abaixo. Projetos que publicaram uma captura de tela ou uma gravação têm preferência, para que a faixa continue visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9493 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2548 · Python · 👁️ observed</sub>
<sub>Encontre os tokens fantasmas. Corrija-os. Sobreviva à compactação. Evite a degradação da qualidade do contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74489 · TypeScript · 👁️ observed</sub>
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
- [Mods: criados com a capacidade de modificação](#mods-criados-com-a-capacidade-de-modificação) — **371**
- [Ecossistemas de plugins do DSH e do Cordis](#ecossistemas-de-plugins-do-dsh-e-do-cordis) — **98**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐150543 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **150543** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9493 · TypeScript · ✅ official · 3 天</summary>

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
| Stars        | **9493**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8261 · Python · ✅ official · 3 天</summary>

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
| Stars        | **8261**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6361 · Python · ✅ official · 243 天</summary>

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
| Stars        | **6361**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1804 · Shell · ✅ official · 3 天</summary>

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
| Stars        | **1804**   |
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 311 天</summary>

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
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2548 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2548**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agentskills` · `claude-code` · `claude-code-mod` · `claude-code-skill` · `claude-plugin` · `codex` · `context-engineering` · `context-window`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐548 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Catálogo comunitário de mods públicos do Claude Code (hooks de função), varridos de GitHub, com o que cada mod pode ler, escrever, executar ou enviar pela rede. Navegue por https://mods.aidojo.si/

<sub>🔧 Encontrado em uso no código: `data/seeds.txt`, `data/duplicates.txt`, `tools/kind.mjs`, `README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **548**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/aqua5230/usage">aqua5230/usage</a></b> · ⭐339 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Fixação de aplicativos na barra de menus e na bandeja de macOS e Windows; exiba Claude Code, Codex, Antigravity e Grok CLI cota, ritmo de consumo e custo na sua tela. Prioriza o uso local, sem chamadas de LLM API. Relatórios HTML, 14 temas.

<sub>🔧 Encontrado em uso no código: `claude_pane/usage-dash/hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | Python                                                                |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **339**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-tools` · `anthropic` · `catppuccin` · `claude` · `claude-code` · `codex` · `cost-tracking` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/6cfdc327f46c7392.png" width="100%" alt="aqua5230/usage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/aqua5230--usage/75f19ddf3cb83f7d.gif" width="100%" alt="aqua5230/usage animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐221 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **221**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐166 · TypeScript · 👁️ observed · 9 天</summary>

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
| Stars        | **166**    |
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
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐164 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code exibe imagens e reproduz vídeos diretamente no seu terminal: capturas de tela, gravações do Playwright e QA sincronizado de antes/depois. Ghostty e kitty.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **164**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐128 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Skins para Claude Code: linhas de ferramentas com ícones, diff, cards de tabela e gráficos Mermaid, uma faixa de uso e quinze temas. /skin troca tudo ao vivo.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **128**    |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐96 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **96**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐79 · TypeScript · 👁️ observed · 4 天</summary>

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
| Stars        | **79**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐77 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **77**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-10 |

🏷 `agent-observability` · `agent-visualization` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/scasella--claude-flightdeck/8c83ca6b4347b2f9.gif" width="100%" alt="scasella/claude-flightdeck animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/darrell-tw/darrelltw-mods">darrell-tw/darrelltw-mods</a></b> · ⭐65 · HTML · 👁️ observed · 7 天</summary>

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
<summary>🧩 <b><a href="https://github.com/0xDarkMatter/claude-mods">0xDarkMatter/claude-mods</a></b> · ⭐62 · Shell · 👁️ observed · 6 天</summary>

##### 📝 Summary

Skills, agentes, comandos, regras, hooks e estilos de saída especializados para Claude Code — continuidade de sessão + ferramentas modernas de CLI para fluxos de desenvolvimento do mundo real

<sub>🔧 Encontrado em uso no código: `justfile`, `skills/auto-skill/SKILL.md`, `skills/task-runner/SKILL.md`, `skills/find-replace/SKILL.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | Shell                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **62**     |
| Last push    | 2026-10-07 |
| First listed | 2026-10-11 |

🏷 `agent-skills` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-skills` · `developer-tools`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐49 · TypeScript · 👁️ observed · 4 天</summary>

##### 📝 Summary

Mods do Claude Code: barras de progresso do plano em tempo real acima do prompt

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **49**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Arjun0014/project-sentinel">Arjun0014/project-sentinel</a></b> · ⭐47 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Centro de controle para execuções longas do Claude Code: progresso do contexto e da execução em uma visão geral, handoffs do Autopilot, proteções e uma visualização tranquila da atividade, no terminal e no Claude Desktop.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **47**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-agents-automation` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/arjun0014--project-sentinel/cd63c979e03573e7.png" width="100%" alt="Arjun0014/project-sentinel screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/henrik-thevibe/Claude-Fables">henrik-thevibe/Claude-Fables</a></b> · ⭐32 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐29 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stars        | **29**     |
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
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐28 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **28**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>gravação animada</sub></td>
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
| Last push    | 2026-10-12 |
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
<summary>🧩 <b><a href="https://github.com/artemnovichkov/xcode-mods">artemnovichkov/xcode-mods</a></b> · ⭐20 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐20 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐18 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mod do Claude Code: Clawd encena o que Claude está fazendo, acima do prompt

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/d6174db0110613e4.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 7 天</summary>

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
| Stars        | **16**     |
| Last push    | 2026-10-05 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/promptadvisers--claude-mods-computer-use-threads/c08dc292e500cd09.png" width="100%" alt="promptadvisers/claude-mods-computer-use-threads screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 10 天</summary>

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
| Stars        | **13**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **12**     |
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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **12**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 27 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 0 天</summary>

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

LINE dentro do Claude Code: o TUI enil como um mod do Claude Code

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
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐9 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Faça o plano Claude Pro durar mais: mods de Claude Code para um HUD de uso exato, saída de shell mais curta e nenhuma releitura de arquivos. Os mods gastam zero tokens.

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
| Last push    | 2026-10-09 |
| First listed | 2026-10-11 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mods` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/176355f2fdfc7ab9.png" width="100%" alt="VedantAndhale/claude-pro-kit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vedantandhale--claude-pro-kit/0e3c2fea33c7be45.gif" width="100%" alt="VedantAndhale/claude-pro-kit animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary><b>Mais nesta categoria</b> <sub>· 337</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Coleção de mais de 100 mods que você pode usar com Claude Code.
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods do Claude e as ferramentas para criá-los: primeiro uma skill de criação…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mods de Claude Code de Ray Amjad: painéis, faixas, proteções de prompt…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - O harness do Claude Code que uso todos os dias, publicado com este nome desde o…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Troque o telhado do Claude Code usando Claude Mods: sem alterar o binário…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatro mods do Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods do Claude Code do Learning Hacker: transforme o funcionamento do agent em…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods do Claude Code que corrigem e traduzem seus prompts antes que Claude os…
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conhecimento do Obsidian com fontes citadas sobre Claude Code mods…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods e skills de Claude Code do Nekyia Labs, criados e usados diariamente por…
- [rashedInt32/glass](https://github.com/rashedInt32/glass) - Uma aparência de aplicativo desktop para a transcrição do terminal do Claude…
- [Jhonatan-de-Souza/ClaudeMods](https://github.com/Jhonatan-de-Souza/ClaudeMods) - Mods de Claude Code: menu de ferramentas Claude, modo Zen, temas de terminal…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Painel lateral do Claude Desktop (aba Code): lista todos os afazeres inacabados…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso acima da caixa de entrada do Claude Desktop (aba Code): cota de 5h…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Um painel lateral para o código Claude: os subagentes executados por uma…
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill que ensina agentes do Claude Code a criar Claude Mods.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins e skills comunitários do Claude, instaláveis em um único mercado.
- [davekiss/mods](https://github.com/davekiss/mods) - Mods do Claude Code por Dave Kiss.
- [devbrother2024/devbrothers-mods](https://github.com/devbrother2024/devbrothers-mods) - Coleção de mods de Claude Code do 개발동생.
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de hooks de função) para Claude Code.
- [Shuffzord/RoadRaven](https://github.com/Shuffzord/RoadRaven) - Seu plano, observando a si mesmo. Árvore de roadmap da área de trabalho local…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - A galeria de mods do Baselane: mods de Claude Code, verificados e fixados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Uma fila de decisões CLI/TUI para humanos que trabalham com agentes…
- [jkf87/ide-mod](https://github.com/jkf87/ide-mod) - Mod do painel IDE do Claude Code: quadro de agentes, árvore de arquivos e…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod do Claude Code que desenha diffs de Edit e Write em duas colunas lado a lado.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown aplicado à caixa de prompt do Claude Code enquanto você digita.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods de Claude Code: painel de uso 像素螃蟹 usage-hud + links HTML clicáveis no…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Um cartão de status flutuante para o Claude Code — modelo, contexto, limites de…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods para o Claude Code: plugins de function-hook que adicionam painéis…
- [chrisluo5311/squad-chat](https://github.com/chrisluo5311/squad-chat) - O plugin completo do Claude Code. Converse com sua equipe, compartilhe código e…
- [Danovich/turntype](https://github.com/Danovich/turntype) - Um teste de digitação para passar o tempo enquanto Claude trabalha.
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nomes e segredos enquanto você…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods e skins para Claude Code: uma barra de progresso ao vivo para as tarefas…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensões do Claude Code. Desbloqueie todo o poder do Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) do Claude Code que adiciona um painel lateral com abas Activity…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Painéis, proteções e mods de qualidade de vida para Claude Code: contexto, uso…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dois mods de Claude Code acima da caixa de prompt: medidor da janela de…
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Leia os arquivos Markdown nomeados pelo código Claude, renderizados ao lado da…
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imagens coladas acima do prompt, em qualquer…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Colega de trabalho por voz para o Claude Code.
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow para Claude Code: uma checklist calma acima do prompt mostrando o…
- [BatuhanCakmakk/wavy-usage](https://github.com/BatuhanCakmakk/wavy-usage) - Anéis de uso preenchidos com líquido acima do prompt do Claude Code: limites de…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, painel de agentes, desfoque PDPA.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, um velocímetro de digitação ao vivo com…
- [charimsma/dopa-mode](https://github.com/charimsma/dopa-mode) - Fogos de artifício para o Claude Code: cada tecla pressionada, chamada de…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para o Claude Code: painéis, comandos e hooks criados com o plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubra mods, plugins e extensões de Claude Code com demonstrações animadas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas mermaid desenhados diretamente na transcrição.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequenos mods do Claude Code (plugins de function-hook): session-switcher e mais.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Uma loja de aplicativos para mods do Claude Code, dentro do Claude Code: /mods…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: limites do plano e contexto acima do prompt, um…
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encontre os mods que você mais usaria)…
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dois mods de Claude Code para executar muitas sessões simultaneamente: um…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de código do Claude sob demanda — uma habilidade que lê sua conversa e…
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubra, inspecione, alterne e atualize mods de Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Melhores mods de Claude Code: selecionados, validados e fixados.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin do Claude Code: roteamento automático de modelos Claude.
- [ElirazKed/claude-code-pr-watch](https://github.com/ElirazKed/claude-code-pr-watch) - Modificação de Claude Code: um painel ao vivo dos PRs do GitHub que uma sessão…
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascote Clawd animado, barras de limite de uso e…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Um marketplace de mods para Claude Code: depurador passo a passo para o loop do…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código de código aberto para o Claude Code: painéis, linhas de status…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - O melhor pacote de mods completo para o Claude Code: limites de uso e HUD de…
- [mthli/cc-shorts](https://github.com/mthli/cc-shorts) - Assista a YouTube Shorts no seu Claude Code 💃.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de ferramentas de Naren para Claude: skills, mods e servidores MCP para o…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, um pequeno mascote pixelado que representa o que…
- [reporails/arcade](https://github.com/reporails/arcade) - Jogos clássicos de desktop como mods de Claude Code, jogados em um painel…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace dos meus mods do Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Uma lista selecionada de mods de código do Claude, instaláveis como um…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Dois mods de Claude Code: cache-keeper e ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantêm um agente honesto — hooks de função que protegem…
- [CodyAMaughan/meme-factory](https://github.com/CodyAMaughan/meme-factory) - Recém-saído da fábrica. Um mod do Claude Code: peça um meme e continue…
- [DarioFontanel/claude-code-mods](https://github.com/DarioFontanel/claude-code-mods) - Mod para o Claude Code: barra de cache de prompts, próximos passos, botões…
- [estruyf/claude-stats-mod](https://github.com/estruyf/claude-stats-mod) - Um mod do Claude Code que desenha seus limites de uso e gastos na faixa acima…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Um mod de Claude Code para capturar pensamentos durante o trabalho…
- [gerricchaplin/pr-pulse](https://github.com/gerricchaplin/pr-pulse) - Status de PR, prontidão para merge, verificações, comentários e alertas de…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Cultive um ovo de chá que ganha sabor lentamente enquanto você escreve código ·…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods do Claude Code de Herman (marketplace herman-mods).
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Veja o que o Claude Code executa em segundo plano: subagentes, tarefas de…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code: responda a Claude ponto por ponto, diretamente no texto.
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo do primeiro dia sobre mods do Claude Code no Windows: uma barra…
- [oborchers/claude-gh-status](https://github.com/oborchers/claude-gh-status) - Mod do Claude Code: status ao vivo de pull requests do GitHub.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod do Claude Code: medidores ao vivo de custo, contexto e cota do plano acima…
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod do Claude Code: um SDLC nativo de IA.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Um mod do Claude Code que ativa ou desativa suas habilidades, agentes, regras e…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods do Claude Code testados e instaláveis com um comando: proteções para o…
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Vários mods do claude code criados por mim.
- [y-hirakaw/claude-code-mods](https://github.com/y-hirakaw/claude-code-mods) - Mods do Claude Code. touch-map: veja quais arquivos Claude listou, leu, editou…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprenda um idioma estrangeiro enquanto trabalha com o código Claude.
- [0xctx/sysop](https://github.com/0xctx/sysop) - Diga ao Claude o que você quer. Receba de volta algo criado, testado, revisado…
- [20alexl/windvane](https://github.com/20alexl/windvane) - Cuida de uma sessão longa do Claude Code para que você não precise: acompanha o…
- [Akeuuh/claude-mods](https://github.com/Akeuuh/claude-mods) - Mercado de plugins do Claude Code: mods baseados em hooks de funções.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de custos, tokens e uso de contexto em tempo real para Claude…
- [bully911210/claude-code-mods](https://github.com/bully911210/claude-code-mods) - Mods de function-hook para o Claude Code: uma linha de telemetria de limites…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Um mod do Claude Code que mantém uma lista atualizada dos itens em aberto em…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods do Claude Code para Engineers de verdade.
- [CrazyCoder/claude-desktop-recap](https://github.com/CrazyCoder/claude-desktop-recap) - Resumo da sessão de terminal do Claude Code, na aba Code do app desktop Claude…
- [DannyW618/What-skills-am-i-using](https://github.com/DannyW618/What-skills-am-i-using) - Mod do Claude Code: veja quais skills, plugins, subagentes e ferramentas MCP…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Veja quais arquivos cada agente do Claude Code tem em seu contexto, e quanto de…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequenos mods do Claude Code para o terminal e o aplicativo desktop.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidade + mod Claude CLI que adiciona palavras em espanhol às respostas do…
- [florian101010/cache-meter](https://github.com/florian101010/cache-meter) - Mod do Claude Code — pare de desperdiçar tokens: /keepwarm.
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Seus eventos do Alarum acima do prompt do Claude Code: o que acabou de chegar e…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Seu backlog Floatee acima do prompt do Claude Code: execute, guie e marque seus…
- [gregdotca/ccmod-the-machine](https://github.com/gregdotca/ccmod-the-machine) - Um mod de código do Claude que o reformula como The Machine de Person of…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod do Claude Code para fluxos de trabalho DAG obrigatórios e…
- [jonyfs/astrolabe](https://github.com/jonyfs/astrolabe) - 🧭 Mod do Claude Code: status da sessão, progresso ao vivo do Spec Kit e…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - A janela de contexto como uma linha acima do prompt, desenhada da forma como o…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod: escolhe o modelo e o esforço de raciocínio de cada subagente.
- [kuehn-lars/cc-graph](https://github.com/kuehn-lars/cc-graph) - cc-graph: um grafo ao vivo sobre o que o Claude Code sabe.
- [kyledarling-io/claude-code-desktop-hud](https://github.com/kyledarling-io/claude-code-desktop-hud) - Um HUD de tarefas ao vivo para o Claude Code Desktop: uma faixa acima do prompt…
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) de Claude Code que faz a interface de terminal do Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Não deixe sua atenção se dispersar enquanto espera pela resposta do Claude Code.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Um plugin gratuito e de código aberto para Claude Code.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Uma fila de prompts para o Claude Code, como mod: /after &lt;task&gt; executa a…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Modificações do Claude Code: selecionadas e testadas, e cada modificação inclui…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Skills do Claude Code: verificador de fatos para documentos, auditor de código…
- [partalemre/MODZ](https://github.com/partalemre/MODZ) - 17 plugins do Claude Code em um único painel.
- [pepperonas/path-links](https://github.com/pepperonas/path-links) - Mod do Claude Code: caminhos clicáveis nas respostas — clique em uma pasta para…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin de companheiro do código Claude: um companheiro ASCII acima do seu…
- [SeongGwangJu/k-mods](https://github.com/SeongGwangJu/k-mods) - Coleção incrível de mods do Claude Code | Coleção de mods do Claude Code.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: um mod de Claude Code que lê em voz alta as respostas de Claude e…
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Dê uma palmada em Claude quando ele fizer besteira — um mod de alívio de…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods do Claude Code: pequenos plugins para painéis ao vivo, roteamento de…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, com comprovantes. Um plugin que planeja, delega e comprova que o…
- [VaitaR/claude-code-limits](https://github.com/VaitaR/claude-code-limits) - Mod do Claude Code: cota de 5h/7d, janela de contexto, tempo restante do cache…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin do Claude Code: monitor de uso, rastreador de tokens e linha de…
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mods do Claude Code: EMCC (Every Mod Claude Code), uma coleção selecionada e…
- [adithepmeekhun/self-clear](https://github.com/adithepmeekhun/self-clear) - Um mod do Claude Code que mantém execuções longas de agentes em andamento: no…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Um gato de braille animado acima do prompt do Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Um gato em pixel acima do seu prompt do Claude Code que executa uma chamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Um mod do Claude Code que escolhe um bom momento para compactar e manter…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods Claude para o Claude Code: token-meter.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de uso geral para o Claude Code: faixas, painéis, toasts e hooks.
- [aott33/model-router](https://github.com/aott33/model-router) - Um mod de Claude Code que escolhe o modelo para cada subagente antes de ele…
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - Um mod do Claude Code: sua janela de contexto em uma linha discreta, cinza até…
- [Ashley-Pettit/lgtm-flash](https://github.com/Ashley-Pettit/lgtm-flash) - As linhas LGTM passam navegando depois de cada alteração de código — um mod do…
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Seus limites de uso do Claude como um cartão de saúde de aldeão animado, com um…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Mods de Claude Code para a equipe S2 (marketplace ather).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Treinos curtos enquanto Claude trabalha: uma meta diária, sequências…
- [aycandv/claude-usage-meter](https://github.com/aycandv/claude-usage-meter) - Um painel de uso para o código Claude: gastos por modelo.
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - Mods do Claude Code de Bakhtiyar Ospanov: plugins criados com base em hooks de…
- [Barncore/agent-watch](https://github.com/Barncore/agent-watch) - Um mod de Claude Code que mostra o que seus subagentes estão fazendo: uma barra…
- [Barncore/turn-timer](https://github.com/Barncore/turn-timer) - Um mod de Claude Code que mostra quanto tempo cada turno levou, em um pequeno…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para o código Claude: Apple Music e Spotify acima do prompt…
- [brahim1o1/claude-turn-profiler](https://github.com/brahim1o1/claude-turn-profiler) - A aba Performance para o Claude Code mostra uma cascata ao vivo de cada…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: relógio de cache, raio de impacto, sugestões, lista de…
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Apenas uma coruja para o seu Claude Code.
- [cerebrai/ironman-mod](https://github.com/cerebrai/ironman-mod) - Um mod do claude code para um fluxo de trabalho aumentado por IA humana — como…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Mantenha o Claude Code dentro de um plano: etapas, portões de aprovação e um…
- [davidurco/cc-tamagotchi](https://github.com/davidurco/cc-tamagotchi) - Um Tamagotchi que vive dentro do Claude Code: ele eclode, come o código que…
- [dricosnyman/claude-favourites](https://github.com/dricosnyman/claude-favourites) - Favoritos para Claude Code: ícones de um clique para seus comandos e habilidades.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Mods do Claude Code (plugins de hooks de função): session-meter e mais.
- [finalpantasy/claude-mod-hider](https://github.com/finalpantasy/claude-mod-hider) - Claude Mod Hider: um pequeno botão que oculta todos os mods do Claude Code…
- [finalpantasy/claude-mod-pack](https://github.com/finalpantasy/claude-mod-pack) - Pacote de mods do Claude: pequenos mods do Claude Code.
- [francktrouillez/claude-freeze](https://github.com/francktrouillez/claude-freeze) - Mod do Claude Code: congele uma sessão e retome-a mais tarde como se nada…
- [GeckoKing9/claude-code-copy-button](https://github.com/GeckoKing9/claude-code-copy-button) - Ctrl+clique para copiar o link em cada bloco de código nas respostas do Claude…
- [guojunjie0614-cyber/workhorse](https://github.com/guojunjie0614-cyber/workhorse) - Mod do Claude Code: delegue tarefas de programação, revisão e operações a Codex…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Um medidor de gastos ao vivo para o Claude Code: o custo da sessão com…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de código do Claude: quanto tempo cada resposta levou, quanto tempo Claude…
- [imsungbin/quackpit-mod](https://github.com/imsungbin/quackpit-mod) - Um cockpit acima do seu prompt do Claude Code. O pato lê os medidores.
- [jasonXiao422/drawing2sw](https://github.com/jasonXiao422/drawing2sw) - Lê automaticamente seus desenhos de engenharia e depois modela no SolidWorks.
- [jBeyondstars/ultracode-models](https://github.com/jBeyondstars/ultracode-models) - Mod do Claude Code: escolha o modelo e o nível de esforço em que cada subagent…
- [JeremyHo1123/claude-code-agent-board](https://github.com/JeremyHo1123/claude-code-agent-board) - Um quadro ao vivo dos subagentes do Claude Code dentro do VS Code: os…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Painel de uso do contexto na barra lateral: total, categorias, crescimento por…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista de arquivos na barra lateral: quais arquivos foram criados, modificados…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, um coelho holandês anão preto e branco em estilo 8-bit, corre e pula acima…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - A seção “O que eu perguntei” na barra lateral: cada frase que o usuário digitou…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linha do tempo na barra lateral: onde o tempo desta rodada foi gasto.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Movimentação de tokens na barra lateral: quantos tokens a conversa principal…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - O “confessionário honesto” do claude code: após responder em cada rodada…
- [jiangnanquan/claude-code-zh](https://github.com/jiangnanquan/claude-code-zh) - Claude Code CLI localização para chinês simplificado (versão autogerenciada)…
- [jidhra/claude-mods](https://github.com/jidhra/claude-mods) - Os mods de Claude Code de Jidhra em um único mercado de plugins.
- [kadaliao/claude-mods](https://github.com/kadaliao/claude-mods) - Mods do Claude Code: plugins de function-hook que alteram a própria interface e…
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive em uma faixa acima do prompt do Claude Code: encena a sessão, mostra…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Um mod que lê em voz alta as respostas e notificações do Claude Code usando…
- [ke11/claude-mods](https://github.com/ke11/claude-mods) - Mods do Claude Code. PixBar: uma criatura pixelada acima do seu prompt que se…
- [KiranPothana/session-board](https://github.com/KiranPothana/session-board) - Mod de Claude Code: todas as sessões do Claude Code em uma janela flutuante…
- [KrasimirKralev/krasi-mods](https://github.com/KrasimirKralev/krasi-mods) - Pequenos mods de Claude Code em um marketplace de plugins.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Um guia de Mods do Claude Code organizado pela comunidade: casos de uso…
- [lucianokatze/mk-usage](https://github.com/lucianokatze/mk-usage) - Mod do Claude Code: os limites do seu plano (sessão de 5h, semana) e a…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Um mod do Claude Code que mostra o que Claude está fazendo no subtítulo da aba…
- [magiclin99/buddy-go](https://github.com/magiclin99/buddy-go) - Buddy, um companheiro não oficial feito por fãs em pixel art que vive acima do…
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - Uma gatinha preta fofinha acima do seu prompt do Claude Code.
- [MarkMerk/markmerk-mods](https://github.com/MarkMerk/markmerk-mods) - Pequenos mods para o Claude Code: runner-avatar, um pequeno avatar que corre…
- [mattbv/intent-ledger](https://github.com/mattbv/intent-ledger) - Mod do Claude Code: um painel ao vivo mostrando o que seu agente de programação…
- [max-gom/claude-session-remover](https://github.com/max-gom/claude-session-remover) - Mod do Claude Code: painel /sessions para navegar e excluir sessões com seus…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Mods comunitários para o Claude Code: proteções, painéis e comandos executados…
- [mkiselyow/diff-lens](https://github.com/mkiselyow/diff-lens) - Mod do Claude Code: peça a Claude para orientar você em um PR, clique em…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code mod: Codex (assinatura do ChatGPT) e outros modelos que não são…
- [MohamedHamed001/claude-mods](https://github.com/MohamedHamed001/claude-mods) - Plugins do Claude Code: delegação.
- [mtami/terminal-tab-title](https://github.com/mtami/terminal-tab-title) - Claude Code mod: nomeia a aba do terminal em que Claude roda.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod do Claude Code que reativa as ferramentas de tarefas pendentes para modelos…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod do Claude Code que espera uma pausa segura e então transfere sua sessão ou…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod do Claude Code: uma linha por tarefa acima do prompt com a tarefa atual…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jogue Connect Four contra uma AI dentro do Claude Code (/connect-four).
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: quando outro agente de programação faz commit no seu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositórios compartilhados por vários agentes de IA…
- [niksavis/handily](https://github.com/niksavis/handily) - Mods do Claude Code que mostram seus itens de trabalho, tarefas e sessões, para…
- [nu0ma/query-guard](https://github.com/nu0ma/query-guard) - Uma proteção para SQL no Claude Code: pergunta antes que Claude execute DELETE…
- [nwilsson/claudepad](https://github.com/nwilsson/claudepad) - Um painel de bloco de notas para Claude Code, como mod.
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - Um mod para Claude Code, Windows e CJK em primeiro lugar: prévias de imagens e…
- [osaki42/awesome-claude-mods](https://github.com/osaki42/awesome-claude-mods) - Os melhores Mods do Claude Code, classificados pelo que fazem por você.
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dois Mods do Claude para o Claude Code: guarda-corpo.
- [partalemre/transceiver](https://github.com/partalemre/transceiver) - Plugin do Claude Code (beta): chat de equipe dentro do Claude Code.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: um Claude Code mod. Worktrees permanentes com início somente…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Painel lateral ao vivo de estatísticas da sessão para a aba Code do aplicativo…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod do Claude Code: flexões para fazer enquanto Claude trabalha. Sem tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: um guia de campo para Claude Code mods, de ELI5 a engenharia de…
- [Ross-cripto/modshelf](https://github.com/Ross-cripto/modshelf) - Um marketplace de código aberto para mods de Claude Code, com skills de…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod do Claude Code: transforma o plano que você aprova no modo de planejamento…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Uma lista selecionada de mods do Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sem custo: os agentes auxiliares rodam no Haiku, e arquivos grandes e logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Uma trilha sonora lofi que acompanha a sessão: calma, foco, fluxo, além de…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprenda enquanto Claude programa: após um turno que alterou o código, uma…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Uma gravação de cada edição feita por Claude: reproduza cada alteração sendo…
- [Showrin/claude-mods](https://github.com/Showrin/claude-mods) - Mods do Claude Code de Showrin para uma rotina diária mais produtiva.
- [sillss1/brain-dash](https://github.com/sillss1/brain-dash) - Claude Code mod: limites de contexto e plano com projeção de taxa de consumo…
- [sohi2212/claude-agent-radar](https://github.com/sohi2212/claude-agent-radar) - Mod do Claude Code: radar ao vivo de agentes em segundo plano + canvas de…
- [someonewithpc/claude-mod-keep-going](https://github.com/someonewithpc/claude-mod-keep-going) - Claude Code mod que mantém sessões não assistidas em andamento apesar de…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Marketplace personalizado de mods do Claude Code (cc-mods), com mods de exemplo…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensagens de commit com um clique para Claude Code com uma Malenia dançante em…
- [SummerRiversound/review-inbox](https://github.com/SummerRiversound/review-inbox) - Mod do Claude Code: PRs aguardando sua revisão, cada um resumido em linguagem…
- [T-AI-Labs/claude-code-mods](https://github.com/T-AI-Labs/claude-code-mods) - Mods para Claude Code. cache-meter: taxa de acerto do cache de prompt…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — uma modificação do Claude Code que mostra o uso do seu plano…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mods não oficiais do Claude Code por tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Um mod do Claude Code que mostra a sessão atual em um painel: cada prompt, o…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Um marketplace de plugins do Claude Code de mods: plugins function-hooks que…
- [thunini/thinking-flow](https://github.com/thunini/thinking-flow) - Um mod do Claude Code que mostra como Claude chegou a cada resposta: sua…
- [tomfluff/claude-read-along](https://github.com/tomfluff/claude-read-along) - Ouça as respostas do Claude Code enquanto a frase lida é destacada.
- [TomySpagnoletti/cc-mods-copy-latest-replies](https://github.com/TomySpagnoletti/cc-mods-copy-latest-replies) - Claude Code mod: um botão abaixo da última resposta de Claude copia todas as…
- [tornikegomareli/claude-whoami](https://github.com/tornikegomareli/claude-whoami) - Modo CC que mostra em qual conta, organização e plano de Claude você está…
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod do Claude Code: faixa de progresso animada e resumo de conclusão para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Três pequenos mods de Claude Code: veja quando seus subagentes terminarão…
- [varunmoka7/disk-sweep](https://github.com/varunmoka7/disk-sweep) - Avisa quando o Mac está com pouco espaço em disco e, com /disk, lista sobras…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Diga &quot;Estou perdido&quot; e Claude explicará novamente sua última resposta em…
- [varunmoka7/park](https://github.com/varunmoka7/park) - Salve esta sessão do Claude Code e escreva uma nota para a próxima.
- [varunmoka7/read-fence](https://github.com/varunmoka7/read-fence) - Impede que Claude abra as pastas de skills, regras e plugins arquivo por…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Faça uma pergunta paralela a Claude em um painel ao lado do seu trabalho.
- [varunmoka7/skills-az](https://github.com/varunmoka7/skills-az) - Exibe uma lista dos seus comandos slash e skills em ordem alfabética assim que…
- [varunmoka7/unattended](https://github.com/varunmoka7/unattended) - Impede que uma sessão do Claude Code faça perguntas quando não há ninguém no…
- [vcdim/claude-code-sciplot](https://github.com/vcdim/claude-code-sciplot) - Um mod do Claude Code para gráficos científicos: Python, R, TikZ, MATLAB e…
- [vmurin/cache-weather](https://github.com/vmurin/cache-weather) - Plugin de Claude Code: contagem regressiva do cache de prompts, taxa de acertos…
- [wonwoo/tool-timeline](https://github.com/wonwoo/tool-timeline) - Um mod do Claude Code que mostra para onde foi o tempo de cada turno: uma linha…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin do Claude Code: seus limites de uso do Claude Pro/Max com previsão de…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para o Claude Code. agent-crew: acompanhe seus subagentes trabalhando como…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Uma coleção selecionada a dedo dos melhores recursos para os agentes mais…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Um plugin do Claude Code que mostra o que está acontecendo — uso de contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Linha de status bonita e altamente personalizável para Claude Code CLI, com…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas as partes do prompt de sistema do Claude Code, 27 descrições de…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Skill de vídeo com IA para Claude Code e Codex — vídeos cinematográficos de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mais de 45 dicas para aproveitar ao máximo o Claude Code, do básico ao avançado…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / habilidade Codex — gere carrosséis para Xiaohongshu e pares de…
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revise o diff do seu agente de programação em um painel do terminal e envie…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin abrangente de linha de status para o Claude Code, com uso de contexto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crie mods para Claude Code: conecte qualquer solicitação, modifique qualquer…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Um painel abrangente de statusline para Claude Code — informações da sessão…
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: acompanhe a pegada de carbono das suas sessões do Claude Code.
- [AwesomeZun/CC-statusline](https://github.com/AwesomeZun/CC-statusline) - Uma linha de status estética para Claude Code, criada por awesomejun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mods públicos para Claude Code.
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash e guias para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs e agentes de programação gratuitos e legais — atualizados…
- [aiedwardyi/claude-usage-monitor](https://github.com/aiedwardyi/claude-usage-monitor) - Plugin de statusline do Claude Code para cota de 5 horas/7 dias, uso de…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Placar ao vivo de futebol, jogos e classificações da competição que você…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill que transforma seu agente de programação em especialista em…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horários de oração, data Hijri, adhkar, ayah diária, jejum sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuração pessoal do Claude Code versionada dentro de ~/.claude — agentes…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Coleção de plugins para Claude Code, pi e DeepSeek Harness: HUD da barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de ferramentas portátil do Claude Code para DDD/Arquitetura Limpa em .NET…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuração global portátil do Claude Code: habilidades personalizadas, hooks…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods não oficiais para a aba Code do Claude Desktop — usage-pet: uma faixa de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins do Claude Code que uso todos os dias: skills e mods, organizados para…
- [vtmocanu/cc-statusline](https://github.com/vtmocanu/cc-statusline) - Statusline ANSI de duas linhas para o Claude Code: contexto de git + k8s…
- [cc-friend/ccost](https://github.com/cc-friend/ccost) - Analise o uso de tokens e os custos do Claude Code a partir de logs de…
- [mkalkere/claude-statusline](https://github.com/mkalkere/claude-statusline) - Linha de status bonita e informativa para Claude Code.
- [abdullahkavakli/let-them-talk](https://github.com/abdullahkavakli/let-them-talk) - Um quadro visual para seus agentes do Claude Code: veja sessões, subagentes e…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Uma linha de status personalizável para Claude Code com um editor de arrastar e…
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins e skills do Claude Code para facilitar mods do jogo…
- [devrim-1283/claude-code-statusline](https://github.com/devrim-1283/claude-code-statusline) - Statusline de uma linha, com código de cores, para o Claude Code — pasta…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizador de painéis divididos para o Claude Code no Windows Terminal e…
- [ian-exnodes/statusbar](https://github.com/ian-exnodes/statusbar) - Plugin do Claude Code: uma linha de status dinâmica de duas linhas abaixo do…
- [jeancarlo-javier/claude-status-bar](https://github.com/jeancarlo-javier/claude-status-bar) - Linha de status ao vivo da fase do fluxo de trabalho para o Claude Code.
- [mvrozanti/claude-progressbar](https://github.com/mvrozanti/claude-progressbar) - Barras de progresso para os comandos Bash executados pelo Claude Code…
- [naturalmoods/herdr-telegram-notify](https://github.com/naturalmoods/herdr-telegram-notify) - Envia mensagens para você no Telegram quando um agent termina ou precisa de…
- [risukisu/claude-code-statusline](https://github.com/risukisu/claude-code-statusline) - Um microdashboard de 3 linhas para o terminal do Claude Code — modelo, consumo…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositório de mods Awesome Media para Claude Code.
- [rootstudioyaml/sprag](https://github.com/rootstudioyaml/sprag) - Reduza os gastos de Claude Code e tokens de Codex: encaminha consultas e…
- [mitre/claude-statusline](https://github.com/mitre/claude-statusline) - Uma linha de status rápida e configurável para o Claude Code — um único binário…
- [barkleesanders/claude-hud](https://github.com/barkleesanders/claude-hud) - HUD em tempo real para o Claude Code — saúde do contexto, atividade das…
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Uma statusline amplificada, com gradação de cores e sem dependências para o…
- [ist-j-ichikawa/claude-code-statusline](https://github.com/ist-j-ichikawa/claude-code-statusline) - Statusline personalizada de j-ichikawa para o Claude Code CLI.
- [kyllian330/claude-statusline](https://github.com/kyllian330/claude-statusline) - Exibe detalhes importantes de status do Claude Code, incluindo modelo…
- [L3DigitalNet/ClaudeCodeStatusLine](https://github.com/L3DigitalNet/ClaudeCodeStatusLine) - Linha de status compacta e mantida ativamente para Claude Code — modelo…
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipes de agentes nativas. Sob controle.
- [Alpinoo/claude-code-usage-statusline](https://github.com/Alpinoo/claude-code-usage-statusline) - Linha de status do PowerShell de Windows para Claude Code: limites de 5 horas e…
- [barnabys-drew/claude-code-statusline](https://github.com/barnabys-drew/claude-code-statusline) - Claude Code statusLine — barras de contexto e limite de taxa diretamente do…
- [black-astro/claude-statusline-astro](https://github.com/black-astro/claude-statusline-astro) - Linha de status do Claude Code — pasta, branch, modelo e uso em uma linha, com…
- [Chy-Zaber-Bin-Zahid/claude-code-statusline](https://github.com/Chy-Zaber-Bin-Zahid/claude-code-statusline) - Uma linha de status do Claude Code com barras de contexto e de uso de 5 horas e…
- [crafts69guy/claude-statusline.nvim](https://github.com/crafts69guy/claude-statusline.nvim) - Linha de status do Claude Code em Lua, com um playground Neovim ao vivo.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline do Claude Code de nível profissional: duração da sessão, custo em…
- [divramod/divramod-claude-code-plugins](https://github.com/divramod/divramod-claude-code-plugins) - Plugins do Claude Code de divramod, um marketplace: skills de agentes e painéis…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Uma linha de status para o Claude Code: contexto, limites e o ritmo da semana…
- [erDevKumar/claude-code-companion](https://github.com/erDevKumar/claude-code-companion) - Extensão de VS Code: progresso de tarefas do Claude Code, ETA e cota de limite…
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Visualize imagens dentro do Claude Code: passe o cursor sobre um chip abaixo de…
- [IceThunder/claude-statusline](https://github.com/IceThunder/claude-statusline) - Linha de status do Claude Code: modelo, barras de cota de 5h/7d, barra de gasto…
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincronize as tarefas de Claude com o Fizzy.do para obter visibilidade da…
- [Kimmihappy793/claude-status-line](https://github.com/Kimmihappy793/claude-status-line) - Exibe uma barra de status detalhada e codificada por cores para o Claude Code…
- [KitchenSink4AI/claude-code-statusline](https://github.com/KitchenSink4AI/claude-code-statusline) - O medidor de contexto do Claude Code: taxa de consumo real, turnos restantes…
- [LounisBou/claude-statusbar](https://github.com/LounisBou/claude-statusbar) - Barra de status de duas linhas para um agente de programação no terminal…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de statusline do Claude Code — rastreia o uso de tokens e o contexto entre…
- [markallisongit/claude-statusline](https://github.com/markallisongit/claude-statusline) - statusline do Claude Code com instalador para Linux e Git Bash no Windows.
- [parisgroup-ai/claude-statusline](https://github.com/parisgroup-ai/claude-statusline) - @parisgroup-ai/claude-statusline — linha de status do Claude Code para macOS +…
- [peaceinitiativemenhadenoil263/claude-status-bar](https://github.com/peaceinitiativemenhadenoil263/claude-status-bar) - Monitore o status do Claude Code na barra de menus do macOS com indicadores em…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Linha de status personalizada do Claude Code.
- [sgarcia-dev/claude-agent-watch](https://github.com/sgarcia-dev/claude-agent-watch) - Painel e linha de status ao vivo para os subagents Codex, OpenCode…
- [silee-tools/claude-statusline](https://github.com/silee-tools/claude-statusline) - HUD de linha de status com pilha vertical independente da largura para o Claude…
- [Sofia-D4L/claude-conf](https://github.com/Sofia-D4L/claude-conf) - Configuração portátil do Claude Code (statusline + instalador).
- [steemandavid/claude-code-statusline](https://github.com/steemandavid/claude-code-statusline) - Linha de status personalizada para Claude Code — modelo, contexto e…
- [Synforger/claude-code-statusline](https://github.com/Synforger/claude-code-statusline) - Linha de status para Claude Code mostrando limites de taxa e uso do contexto de…
- [t4t5u0/claude-statusline](https://github.com/t4t5u0/claude-statusline) - Linha de status de 4 linhas para Claude Code.
- [thaiquangquy/claude.me](https://github.com/thaiquangquy/claude.me) - Configuração portátil do Claude Code: CLAUDE.md, settings, statusline, skills.
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine Multi-Protocolo Universal, Autoaprendizado de Contexto e Plugin…
- [Undone-drawknife974/claude-code-statusline](https://github.com/Undone-drawknife974/claude-code-statusline) - Acompanhe o uso de contexto do Claude Code, os custos da sessão e as…
- [wcampbell-dw/claude-plugins](https://github.com/wcampbell-dw/claude-plugins) - Plugins do Claude Code: spinners de subagentes em tempo real, uma linha de…
- [whr819987540/claude-sync-settings](https://github.com/whr819987540/claude-sync-settings) - Sincronização entre várias máquinas da configuração em nível de usuário do…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de deterioração de contexto 2026 — Monitor proativo de memória de IA e…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes e linhas de status do Claude Code: coleções e ferramentas de…
- [tronschell/statusline.sh](https://github.com/tronschell/statusline.sh) - Um criador visual para statuslines de código do Claude.
- [Magnus-Gille/tokenatlas](https://github.com/Magnus-Gille/tokenatlas) - Statusline do Claude Code mostrando o uso de tokens em tempo real e o consumo…
- [lexfrei/ailine](https://github.com/lexfrei/ailine) - Statusline do Claude Code com limites reais de uso de Anthropic API.
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: painéis, faixas e companheiros baseados em hooks de…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passe tarefas entre suas sessões do Claude Code.
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Isto em um servidor MCP para controlar o MODS, a ferramenta modular…
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encontre o que você pede ao Claude Code repetidamente e transforme…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Biblioteca de 3 skills para o Claude Code: session-handoff, session-statusline…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex e Claude Code para traduzir mods de CK3 com um LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código aberto e outras extensões para Claude Code.

</details>

<a id="dsh-cordis"></a>

## Ecossistemas de plugins do DSH e do Cordis

DeepSeek Harness e Cordis chegam ao mesmo lugar por uma direção diferente: para eles, o plugin é o mecanismo de modificação; portanto, um plugin lá equivale a um mod aqui.

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74489 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74489**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐184903 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **184903** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `ctf`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐100875 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **100875** |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐82831 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **82831**  |
| Last push    | 2026-10-12 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35774 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35774**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30656 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Solução moderna para desktop criada para o ecossistema de plugins do DeepSeek Harness (DSH). Tudo é um «plugin»; o próprio desktop também é um «plugin».

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30656**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25562 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Distilly — destile como eles pensam em Skills reutilizáveis para qualquer Agent ou Bot. Anteriormente Colleague Skill（antigo Colleague Skill）.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **25562**  |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-skills` · `agentic-ai` · `ai-agent` · `ai-agents` · `ai-assistants` · `ai-persona` · `claude-code` · `claude-skills`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/titanwings--distilly/1e118bb52fdcbd1c.png" width="100%" alt="titanwings/distilly screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9157 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Meta-framework de composabilidade espaço-temporal

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **9157**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8691 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Ecossistema de agregação de plugins Web do DeepSeek Harness (DSH) · Tudo é plugin, distribuído pela Creative Workshop｜｜Ecossistema de agregação de plugins Web do DeepSeek Harness (DSH) · Tudo é um plugin, distribuído pela Creative Workshop

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8691**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4532 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

O plugin TUI oficialmente mais recomendado do DSH — alto desempenho, baixo consumo, uma simpática baleia pixelada e interação fluida com o mouse. Instalação com um comando via npm. / Plugin TUI oficialmente mais recomendado pelo DSH, alto desempenho e baixo consumo, simpática baleia pixelada, interação fluida com o mouse, instalação com um comando via npm

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4532**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/strukto-ai/mirage">strukto-ai/mirage</a></b> · ⭐3684 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

O primeiro Terminal Virtual do mundo para Agentes de IA

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3684**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-sandbox` · `agent-tools` · `ai-agents` · `bash` · `claude-code` · `dsh` · `dsh-plugin` · `fuse`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whiteguo233/OpenBiliClaw">whiteguo233/OpenBiliClaw</a></b> · ⭐3422 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Agent de descoberta de conteúdo de IA multiplataforma, de código aberto, privado e local-first, com autoevolução: primeiro entende você e depois busca proativamente conteúdo no Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo e na Web aberta. (compatível com o plugin deepseek harness) | Agent de descoberta de conteúdo de IA multiplataforma, de código aberto e local-first: entende você e depois encontra proativamente conteúdo no Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo e na Web aberta. (compatível com o plugin deepseek harness)

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3422**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agent` · `bilibili` · `chrome-extension` · `content-discovery` · `cross-platform` · `deepseek-harness` · `douyin` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/00bf0e70f2903777.png" width="100%" alt="whiteguo233/OpenBiliClaw screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whiteguo233--openbiliclaw/c7c275524e19b917.gif" width="100%" alt="whiteguo233/OpenBiliClaw animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2064 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

O melhor plugin do DeepSeek Harness para análise e gerenciamento de contexto, com painel de contexto / navegador / barra lateral e comando de contexto, para estatísticas, composição, detalhamento e evolução do contexto, permitindo entender como ele é composto e como evolui. Plugin completo de visualização de contexto do DeepSeek Harness, com painel Context, navegador e barra lateral, além do comando Context, oferecendo uma visão detalhada da composição, evolução, compressão, poda e outros eventos e ações do contexto.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2064**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xmanrui/dsh-im">xmanrui/dsh-im</a></b> · ⭐1942 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Conecte robôs de IM ao DeepSeek Harness por código QR ou credenciais (9 canais): Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord e WhatsApp.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1942**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-agents` · `chatbot` · `cordis` · `deepseek` · `deepseek-harness` · `dingtalk-bot` · `discord-bot` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xmanrui--dsh-im/cba81787088f67af.jpg" width="100%" alt="xmanrui/dsh-im screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1185 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1185**   |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/shengsheng90/DSH-taskboard">shengsheng90/DSH-taskboard</a></b> · ⭐334 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin Taskboard local nativo para DeepSeek Harness. Projetos baseados em SQLite, reivindicação/revisão por Agent e uma Web UI nativa — sem iframe e sem um segundo runtime de chat.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **334**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `task-management` · `taskboard`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/shengsheng90--dsh-taskboard/641e63303f0eed9c.png" width="100%" alt="shengsheng90/DSH-taskboard screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/RevolutionLA/dsh-dream-skin">RevolutionLA/dsh-dream-skin</a></b> · ⭐231 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin de personalização de aparência / papel de parede / pacote de temas do DeepSeek Harness (dsh-plugin) — 8 temas Mirage, cor de destaque por usuário, Wallpaper 2.0, importação e exportação de pacotes de temas / links de compartilhamento, favoritos e aleatoriedade, tudo implementado com um sistema de tokens totalmente nativo.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **231**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugin-theme` · `skin` · `theme` · `wallpaper`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/revolutionla--dsh-dream-skin/9ae1ef97a89d3ff0.png" width="100%" alt="RevolutionLA/dsh-dream-skin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐205 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin nativo do DeepSeek Harness (DSH) que integra TypeSafe Jev ou uma API de decisão como luna como camada de decisão System One para seleção, supervisão, correções e aprovações de agentes.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **205**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐186 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin de backup e restauração do DeepSeek Harness (DSH) — exporte, importe, migre e sincronize sua configuração completa do DSH, plugins, servidores MCP, skills e workspace. Migração para outra máquina com um clique.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **186**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/52a2f3587f8e40b4.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐124 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin de mascote de mesa do DeepSeek Harness: uma baleia energética acompanha você enquanto programa 🐋 Compatível com o cliente desktop DSH 0.2.0-rc.2 e com a versão Web antiga (desktop pet / mascot, local-first)

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **124**    |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/youdotcom-oss/agent-skills">youdotcom-oss/agent-skills</a></b> · ⭐89 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Skills e plugins do You.com para pesquisa na web, extração de conteúdo, pesquisa, finanças e descoberta de integrações, ajudando agentes de AI a trabalhar com contexto web atualizado.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **89**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-plugins` · `agent-skills` · `ai-agents` · `claude-code` · `codex` · `cordis` · `cursor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/youdotcom-oss--agent-skills/894c769a60cbc23c.png" width="100%" alt="youdotcom-oss/agent-skills screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace">dsh-wsl-workspace-maintainers/dsh-wsl-workspace</a></b> · ⭐80 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Suporte a espaços de trabalho WSL para o DeepSeek Harness — uma experiência perfeita de uso de espaços de trabalho WSL, sem precisar instalar outro dsh dentro do WSL. Depois de instalar este plugin, basta adicionar um espaço de trabalho WSL diretamente pela GUI. Suporte a espaços de trabalho WSL para o DeepSeek Harness — desfrute de uma experiência perfeita de espaço de trabalho WSL sem precisar instalar o dsh dentro do WSL. Depois que este plugin for instalado, você poderá adicionar diretamente um espaço de trabalho WSL pela GUI.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **80**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-wsl-workspace-maintainers--dsh-wsl-workspace/252926072330fff2.png" width="100%" alt="dsh-wsl-workspace-maintainers/dsh-wsl-workspace screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐72 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Versão desktop do Agent criada com base no núcleo do Deepseek-Harness. Herda todos os recursos do núcleo e complementa as funções relacionadas a IDE.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **72**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐59 · HTML · 🔎 inferred · 0 天</summary>

##### 📝 Summary

O diretório vivo de plugins do DeepSeek Harness — atualizado a cada hora, testado diariamente quanto à compatibilidade, com loja de plugins e scaffolder integrados. Diretório vivo de plugins do DSH: atualização por hora, testes diários de compatibilidade, loja de plugins e scaffolder integrados.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | HTML                                                                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **59**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PolinniZhong/dsh-knit">PolinniZhong/dsh-knit</a></b> · ⭐54 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Recuperação de contexto do workspace orientada à tarefa e rastreamento do ciclo de vida para AI coding agents. Encontre, organize e acompanhe o contexto do workspace mais relevante para a tarefa atual — localmente, de forma determinística, sem chamadas de modelo e sem rede.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-better-sidebar`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/e98f690af54d1e8d.png" width="100%" alt="PolinniZhong/dsh-knit screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/polinnizhong--dsh-knit/338cb6ef3e90368c.gif" width="100%" alt="PolinniZhong/dsh-knit animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-guide">PerryLink/dsh-plugin-guide</a></b> · ⭐50 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Base de conhecimento para desenvolvimento de plugins do DeepSeek Harness (dsh): o guia de desenvolvimento em 10 capítulos, manual de lançamento, problemas upstream não corrigidos verificados na fonte e dados medidos do ecossistema — instalável como um pacote DSH.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **50**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `agent-skill` · `ai-agent` · `ai-agents` · `checker` · `cli` · `cordis` · `deepseek` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/d665a08f58e38532.png" width="100%" alt="PerryLink/dsh-plugin-guide screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-guide/3aee78fb7bcfc697.gif" width="100%" alt="PerryLink/dsh-plugin-guide animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HOWILLMAKEIT/dsh-model-context-catalog">HOWILLMAKEIT/dsh-model-context-catalog</a></b> · ⭐34 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin do DeepSeek Harness: corresponde modelos a janelas de contexto com um clique, exibe a origem da capacidade e permite configuração em lote por seleção, gerenciamento de janelas existentes e edição manual.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **34**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/gjj-star/dsh-conversation-navigator">gjj-star/dsh-conversation-navigator</a></b> · ⭐23 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Navegação de sessões do DSH

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `dsh` · `dsh-plugin` · `dsh-plugins` · `ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/gjj-star--dsh-conversation-navigator/4aef8cb83b546a1c.png" width="100%" alt="gjj-star/dsh-conversation-navigator screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/HaoyueQin/dsh-usage-statistics-panel">HaoyueQin/dsh-usage-statistics-panel</a></b> · ⭐23 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin web do DSH: estatísticas diárias de uso de tokens com um mapa de calor de atividade no estilo GitHub, curva de taxa de acertos do cache e detalhamento por modelo

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **23**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `cordis` · `data-visualization` · `deepseek-harness` · `dsh-plugin` · `llm` · `plugin` · `react` · `settings-panel`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/haoyueqin--dsh-usage-statistics-panel/e57757e1005cbc5b.png" width="100%" alt="HaoyueQin/dsh-usage-statistics-panel screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/liustack/pptwise">liustack/pptwise</a></b> · ⭐21 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Um PowerPoint de verdade, não HTML. Diga à sua IA o que abordar e o pptwise cria uma apresentação editável na sua própria máquina. Habilidade de agente + plugin DSH, sem conta e sem chave API para renderizar. | Um PPT de verdade, não HTML. Diga à IA o que apresentar e o pptwise fará um PPT editável no seu próprio computador. Habilidade de agente + plugin DSH, sem cadastro e sem chave API para renderizar.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **21**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-04 |

🏷 `agent-skill` · `agent-skills` · `ai-agent` · `claude-code` · `claude-skills` · `codex` · `cordis` · `deck-generation`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/liustack--pptwise/e6f193d6fc2ea355.png" width="100%" alt="liustack/pptwise screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/KannaKuron/dsh-better-workspace">KannaKuron/dsh-better-workspace</a></b> · ⭐18 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Plugin web do DSH: uma árvore hierárquica de workspaces para a barra lateral — títulos contendo / são agrupados em pastas virtuais; o fluxo de adição de workspace recebe um pop-up de grupo pai

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18**     |
| Last push    | 2026-10-12 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `sidebar` · `tree` · `workspace`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kannakuron--dsh-better-workspace/83cddff440dfe49a.png" width="100%" alt="KannaKuron/dsh-better-workspace screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vecnode/vncode">vecnode/vncode</a></b> · ⭐8 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

vncode 🤖 IDE Agent-Human ⌨️ versões Web e Desktop, com Plugins, Skills e Interfaces incluídos.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **8**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-skills` · `deepseek-ai` · `deepseek-api` · `deepseek-chat` · `deepseek-harness` · `dsh` · `dsh-plugin` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vecnode--vncode/73837d3e9e3dc179.png" width="100%" alt="vecnode/vncode screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/unStone/dsh-xray">unStone/dsh-xray</a></b> · ⭐7 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Raio X dos plugins do DeepSeek Harness: capacidades declaradas versus comportamento real. Registro + scanner estático + badges.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **7**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/alone-tree/dsh-skill-mcp-manager">alone-tree/dsh-skill-mcp-manager</a></b> · ⭐6 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

能力库 (Capability) — gerenciamento visual completo de DSH Skills e MCP: carregamento de MCP sob demanda, hot reload durante a sessão e descrições de SKILL/MCP visualizáveis no plugin.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6**      |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `mcp` · `skill`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/alone-tree--dsh-skill-mcp-manager/bc0fce1b6eabef09.png" width="100%" alt="alone-tree/dsh-skill-mcp-manager screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 64</sub></summary>

- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) - Responda-me com HTML — uma habilidade de agent que responde a perguntas…
- [anywhere-labs/Agents-Anywhere](https://github.com/anywhere-labs/Agents-Anywhere) - Workbench de Agent de código aberto e entre dispositivos.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Uma proteção pré-execução para agentes de programação com AI.
- [LivXue/dsh-plugin-shop](https://github.com/LivXue/dsh-plugin-shop) - O mercado de plugins do DeepSeek Harness mais completo — atualizado…
- [hashgraph-online/awesome-ai-plugins](https://github.com/hashgraph-online/awesome-ai-plugins) - Uma lista selecionada dos melhores plugins incríveis de IA para assistentes de…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 Uma biblioteca de microlessons para AI Agents, sem dependências e respaldada…
- [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) - Plugin do DSH — modelos OpenCode Zen gratuitos para o DeepSeek Harness (DSH).
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins DSH / DSH Plugin Marketplace: navegue, instale e atualize…
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - Narrativa interativa 18+ com quebra de armadura integrada ao DeepSeek: NPCs com…
- [jaccen/Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) - Artigos sobre computação gráfica, 3DGS e inteligência espacial, atualizados…
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Vem instalado com 27 habilidades de engenharia e produtividade de…
- [arcships/rutis](https://github.com/arcships/rutis) - Um runtime de plugins para softwares que iteram sobre si mesmos — a base onde…
- [JingbiaoMei/Tokdash](https://github.com/JingbiaoMei/Tokdash) - Painel do Agent: visualização e análise de sessões e uso de cotas.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Diretório selecionado de plugins do DeepSeek Harness (DSH) — mais de 280…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin do DSH: shell Git Bash para todos os modos de agente em Windows…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agente de chat em grupo multiplataforma baseado no…
- [dphmoblie/deepseek-harness-android](https://github.com/dphmoblie/deepseek-harness-android) - dsh para Android: integra DeepSeek Harness, ambiente de execução Ubuntu…
- [FeatherHunter/dsh-im-companion](https://github.com/FeatherHunter/dsh-im-companion) - dsh-im-companion: aprimora o dsh-im com os conceitos de assistente e lar — veja…
- [Y1X1n/dsh-prompt-optimizer](https://github.com/Y1X1n/dsh-prompt-optimizer) - Plugin do DeepSeek Harness · botão «Otimizar» com um clique na barra de envio…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, ferramentas, habilidades e recursos de aprendizado do DeepSeek Harness…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociação comercial A2A + plugin do DeepSeek Harness (dsh).
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - A IA argumenta. O código decide. As perdas permanecem na página.
- [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) - Plugin de memória de projeto em tempo de leitura para o DeepSeek Harness (dsh).
- [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) - Plugin do DeepSeek Harness: transforma conversas automaticamente em cartões de…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Registro de plugins, pacotes e habilidades do DeepSeek Harness (dsh), com dados…
- [realguan/dsh-dock](https://github.com/realguan/dsh-dock) - Central de controle desktop multiplataforma criada especialmente para o…
- [dsh-plugin-lab/dsh-zhihu-search](https://github.com/dsh-plugin-lab/dsh-zhihu-search) - Plugin do DSH: três ferramentas criadas com o API oficial da plataforma aberta…
- [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) - Testes contínuos de compatibilidade para plugins do DeepSeek Harness: versões…
- [xiaoshenming/dsh-session-surgeon](https://github.com/xiaoshenming/dsh-session-surgeon) - Repare sessões do DeepSeek Harness que se recusam a carregar.
- [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) - Uma lista selecionada de plugins, ferramentas, skins e extensões para o…
- [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) - Plugin do DSH: painel Git no estilo IDE dentro da GUI Web — visão geral de…
- [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) - Plugin de aprimoramento da Web UI do DSH + shell desktop Electron sem bordas.
- [dsh-plugin-lab/dsh-workbuddy-bridge](https://github.com/dsh-plugin-lab/dsh-workbuddy-bridge) - Plugin do DSH: conecta os modelos do aplicativo desktop WorkBuddy ao DeepSeek…
- [EdwinZDZ/dsh-api-balance-ring](https://github.com/EdwinZDZ/dsh-api-balance-ring) - Um anel de saldo do DeepSeek API em tempo real para o compositor do DeepSeek…
- [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) - Workspace com várias pastas: permite que o Agent do DSH (DeepSeek Harness) leia…
- [dsh-pub/dsh-pub](https://github.com/dsh-pub/dsh-pub) - O registro e instalador bilíngue, com fontes, do ecossistema de plugins do…
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - Plugin DSH: uma janela de ferramentas Git de nível IDE como uma aba nativa do…
- [mjylfz/dsh-skill-mover](https://github.com/mjylfz/dsh-skill-mover) - Transfira com um clique as habilidades de outros Agents para o DeepSeek…
- [xiaoso456/dsh-workflow-lite](https://github.com/xiaoso456/dsh-workflow-lite) - Plugin de fluxo de trabalho flexível do DeepSeek Harness: desenhe o fluxo em…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Veja claramente cada ação observável dos agentes de codificação de IA.
- [Aliuyanfeng/dsh-soul](https://github.com/Aliuyanfeng/dsh-soul) - O plugin DeepSeek Harness Personalization Settings é usado para configurar o…
- [cv-superding/dsh-webin](https://github.com/cv-superding/dsh-webin) - Plugin não oficial do DSH: controle UIs web de IA (DeepSeek/Qwen/...) em um…
- [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) - Plugin adaptador de terceiros: registra o serviço MCP do REA upstream.
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - Coleção de plugins DSH: autenticação por senha + confiança para acesso web de…
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Padrão de verificação sem dependências para plugins do DeepSeek Harness (dsh)…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Ecossistema de plugins do DeepSeek Harness: 86 plugins de código aberto em uma…
- [SuCriss/dsh-leekbox](https://github.com/SuCriss/dsh-leekbox) - LeekBox — assistente para acompanhar ações A · plugin Web do DeepSeek Harness…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web do DeepSeek Harness (DSH): aba lateral market-dashboard para…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode no DeepSeek Harness — plugin DSH que mantém OpenCode Zen + modelos de…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins de terceiros e gerenciador protegido do…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx é uma bancada de trabalho desktop extensível e centrada nas pessoas…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - Um agente de codificação completo para o DeepSeek Harness — fluxos de trabalho…
- [dsh-plugin-lab/dsh-ds-balance](https://github.com/dsh-plugin-lab/dsh-ds-balance) - Plugin do DSH: mostra o saldo da sua conta DeepSeek na parte inferior da barra…
- [iluluyu/dsh-ui-outline](https://github.com/iluluyu/dsh-ui-outline) - Plugin de navegação de turnos na borda direita, no estilo do ChatGPT, para o…
- [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) - dsh-minato — pacote comunitário de implantação e operação local para DeepSeek…
- [Wenston-dev/awesome-dsh-plugin](https://github.com/Wenston-dev/awesome-dsh-plugin) - Lista incrível de plugins dsh — diretório automatizado de plugins do DeepSeek…
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin do DeepSeek Harness: transforma a falha de provisionamento da ACL da…
- [argszero/cordis-plugin-tool-deadline-guard](https://github.com/argszero/cordis-plugin-tool-deadline-guard) - Prazos em nível de implantação para chamadas de ferramenta dsh que não declaram…
- [fshoocn/cordis-port](https://github.com/fshoocn/cordis-port) - Port do Python para o pacote principal do Cordis · runtime baseado em plugins /…
- [xinvxueyuan/cordis-plugin-github](https://github.com/xinvxueyuan/cordis-plugin-github) - Plugin Cordis / DeepSeek Harness — ferramentas GitHub API normalizadas para…
- [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) - Distribuição desktop instalável do DeepSeek Harness baseada em Tauri, com…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.
- [LittleCar30/dsh-deepseek-web](https://github.com/LittleCar30/dsh-deepseek-web) - Plugin desktop independente do dsh para controlar o DeepSeek Web por meio de um…

</details>

<a id="writing"></a>

## Textos, discussões e vídeos

Textos, discussões e vídeos sobre a capacidade de mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925102">Claude Code Mods</a></b> · ⭐6 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49926243">Getting started with Claude Code mods</a></b> · ⭐3 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐3 · 👁️ observed · 9 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49971594">Terminal Steps: A Claude mod for a daily step goal, synced from Apple Health</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 3 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49927599">Pi-autoresearch ported to Claude Code 1:1 using the new mods API</a></b> · ⭐2 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 10 天</summary>

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
| TypeScript | 296      | `anthropics/claude-code`, `anthropics/claude-code-action`, `hamzafer/claude-code-mods`                        |
| JavaScript | 72       | `karanb192/awesome-claude-code-mods`, `karanb192/claude-code-mods`, `ucsandman/claude-harness`                |
| Python     | 45       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 25       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 13       | `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`, `testy-cool/awesome-claude-code-mods`                     |
| Rust       | 6        | `persiyanov/herdr-reviewr`, `cc-friend/ccost`, `arcships/rutis`                                               |
| Go         | 4        | `mitre/claude-statusline`, `lexfrei/ailine`, `esengine/DeepSeek-Reasonix`                                     |
| PowerShell | 2        | `markallisongit/claude-statusline`, `czcdr/dsh-plugin-rea`                                                    |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `sakanamaru/dsh-minato`                                                                                       |
| Kotlin     | 1        | `dphmoblie/deepseek-harness-android`                                                                          |
| Lua        | 1        | `crafts69guy/claude-statusline.nvim`                                                                          |
| Swift      | 1        | `peaceinitiativemenhadenoil263/claude-status-bar`                                                             |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Correções são bem-vindas e são a maneira mais rápida de melhorar esta lista. Abra uma issue ou um pull request se uma entrada estiver na categoria errada, com a classificação errada ou se um projeto tiver sido excluído indevidamente por colisão de nome — essa é a categoria em que filtros automatizados têm maior probabilidade de errar.

---

<sub>Projeto independente da comunidade. Não afiliado, endossado nem revisado por Anthropic. Claude Code, Claude e Anthropic são marcas registradas de Anthropic. O comportamento do produto pode mudar sem aviso; verifique tudo o que for essencial na documentação oficial. Os ativos permanecem propriedade de seus projetos de origem e são reproduzidos somente quando uma licença permite.</sub>

<sub>Last updated · 2026-10-13T21:42:20+08:00</sub>
