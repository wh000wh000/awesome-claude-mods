<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods incríveis do Claude">
</p>

<h1 align="center">Mods incríveis do Claude</h1>

<p align="center"><b>O índice de mods e plugins do Claude Code classificados por evidências, além dos comportamentos mais profundos que eles alteram.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-597-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Português</b> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice ativo** · Última sincronização: `2026-10-16T23:45:14+08:00` (UTC+8)
> · Entradas: **597** · Adicionadas na atualização mais recente: **0** · Linguagens de implementação: **13**

<sub>Cada entrada abaixo foi coletada, filtrada e verificada novamente de forma automática. Nada aqui é uma inserção paga.</sub>

<a id="featured"></a>

## Destaques do momento

<sub>Uma entrada por categoria, classificada pelo grau de evidência e pelo número de estrelas, recalculada a cada atualização. É uma classificação, não uma recomendação; cada destaque leva ao respectivo card completo abaixo. Projetos que publicaram uma captura de tela ou uma gravação têm preferência, para que a faixa continue visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9534 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2575 · Python · 👁️ observed</sub>
<sub>Encontre os tokens fantasmas. Corrija-os. Sobreviva à compactação. Evite a degradação da qualidade do contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐75482 · TypeScript · 👁️ observed</sub>
<sub>🌊 O agent harness original. Implante enxames inteligentes multiagente, coordene fluxos de trabalho autônomos e crie sistemas de IA conversacional. Inclui memória…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐16 · 👁️ observed</sub>
</td>
</tr>
</table>

## Conteúdo

- [O que é um mod do Claude Code](#o-que-é-um-mod-do-claude-code)
- [Como as entradas são classificadas](#como-as-entradas-são-classificadas)
- [Oficial: repositórios próprios de Anthropic e notas de versão](#oficial-repositórios-próprios-de-anthropic-e-notas-de-versão) — **17**
- [Mods: criados com a capacidade de modificação](#mods-criados-com-a-capacidade-de-modificação) — **467**
- [Ecossistemas de plugins do DSH e do Cordis](#ecossistemas-de-plugins-do-dsh-e-do-cordis) — **105**
- [Textos, discussões e vídeos](#textos-discussões-e-vídeos) — **8**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151200 · TypeScript · ✅ official · 0 天</summary>

##### 📝 Summary

Claude Code é uma ferramenta de programação agêntica que funciona no seu terminal, entende sua base de código e ajuda você a programar mais rápido executando tarefas rotineiras, explicando códigos complexos e gerenciando fluxos de trabalho do git — tudo por meio de comandos em linguagem natural.

<sub>🔧 Encontrado em uso no código: `feed.xml`, `mods/diff/README.md`, `mods/diff/hooks/host/host.ts`</sub>

##### 📌 Basic facts

| Field     | Value                                                           |
| --------- | --------------------------------------------------------------- |
| Category  | `Oficial: repositórios próprios de Anthropic e notas de versão` |
| Evidence  | `publicado pelo próprio Anthropic`                              |
| Linguagem | TypeScript                                                      |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **151200** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9534 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **9534**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8291 · Python · ✅ official · 0 天</summary>

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
| Stars        | **8291**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6398 · Python · ✅ official · 246 天</summary>

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
| Stars        | **6398**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1813 · Shell · ✅ official · 0 天</summary>

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
| Stars        | **1813**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 314 天</summary>

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
<summary><b>Mais nesta categoria</b> <sub>· 5</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Adicionado `$.ui.notify` aos mods: emite uma notificação nativa usando sua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corrigido o Esc ou uma interrupção durante um hook de `UserPromptSubmit` ou o…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.
- [Claude Code 2.1.301 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `rows` to a mod.

</details>

<a id="mods"></a>

## Mods: criados com a capacidade de modificação

Cada entrada aqui apresenta evidências do uso da capacidade que o Claude Code adquiriu na versão 2.1.287: ela desenha por meio de `ui.render`, possui um painel, faixa ou cartão, lê `$.ui.selection()`, cria companheiros de equipe com `agent.spawn` ou afirma claramente que é um mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2575 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2575**   |
| Last push    | 2026-10-16 |
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
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐892 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Custom Claude Code Mods that I need

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **892**    |
| Last push    | 2026-10-14 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐612 · JavaScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Catálogo comunitário de mods públicos do Claude Code (hooks de função), varridos de GitHub, com o que cada mod pode ler, escrever, executar ou enviar pela rede. Navegue por https://mods.aidojo.si/

<sub>🔧 Encontrado em uso no código: `data/duplicates.txt`, `tools/kind.mjs`, `README.md`, `finder/README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **612**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐262 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **262**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐219 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Claude Code plugin to see, review and iterate on your agent's work without leaving the terminal: show images, play videos, and run visual QA with Playwright recordings and before/after comparisons inside the Claude Code terminal. Works in any terminal that supports the kitty graphics protocol, fully cross-platform on macOS, Linux and Windows.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **219**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agentic-coding` · `ai-agents` · `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/iamumeransari--claude-show-your-work/7a0af2143a7dfd15.jpg" width="100%" alt="iamumeransari/claude-show-your-work screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐212 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Mods for Claude Code. effortless picks the reasoning effort for every prompt and shows the cache countdown. textless (desktop app) shows art, quotes and chess instead of the wall of text while Claude works.

<sub>🔧 Encontrado em uso no código: `docs/agent-panel/PLAN.md`, `hooks/register.tsx`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | HTML                                                                  |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **212**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-tools` · `anthropic` · `chess` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐198 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **198**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐153 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **153**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐116 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **116**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐95 · TypeScript · 👁️ observed · 4 天</summary>

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
| Stars        | **95**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 7 天</summary>

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
| Stars        | **80**     |
| Last push    | 2026-10-08 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🧩 <b><a href="https://github.com/whyashthakker/awesome-claude-code-mods">whyashthakker/awesome-claude-code-mods</a></b> · ⭐73 · TypeScript · 👁️ observed · 13 天</summary>

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
| Stars        | **73**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

🏷 `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐54 · JavaScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

Mods do Claude Code: barras de progresso do plano em tempo real acima do prompt

<sub>🔧 Encontrado em uso no código: `README.md`, `README.zh-CN.md`, `README.es.md`, `README.de.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | JavaScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **54**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐36 · TypeScript · 👁️ observed · 1 天</summary>

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
| Stars        | **36**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `claude-code` · `claude-code-plugin` · `claude-mods` · `function-hooks`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/d6ee96dd984886df.png" width="100%" alt="oikon48/prompt-rail screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/oikon48--prompt-rail/87309761ea9d1f19.gif" width="100%" alt="oikon48/prompt-rail animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NovusEdge/glowup">NovusEdge/glowup</a></b> · ⭐30 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A glow-up for Claude Code: a live cockpit pane, shareable themes, and a pixel pet that acts out what Claude is doing

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `developer-tools` · `eye-candy` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/52396333a085f3d5.gif" width="100%" alt="NovusEdge/glowup screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/novusedge--glowup/4905ed24c2c755ad.gif" width="100%" alt="NovusEdge/glowup animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐30 · TypeScript · 👁️ observed · 1 天</summary>

##### 📝 Summary

A Claude Code mod: Claude assigns you the tasks only you can do. They wait in a pane until you answer, and your answer goes back to Claude.

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **30**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/80234f85f660a0df.gif" width="100%" alt="tzafrir/human-in-the-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tzafrir--human-in-the-loop/ba055747f756e694.gif" width="100%" alt="tzafrir/human-in-the-loop animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 2 天</summary>

##### 📝 Summary

Mods de Claude Code: menu de ferramentas Claude, modo Zen, temas de terminal, controles de esforço e modo

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **24**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen.png" width="100%" alt="Jhonatan-de-Souza/ClaudeMods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Jhonatan-de-Souza/ClaudeMods/main/docs/screenshots/zen-demo.gif" width="100%" alt="Jhonatan-de-Souza/ClaudeMods animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **22**     |
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
<summary>🧩 <b><a href="https://github.com/BrianHuang813/clawd-actor">BrianHuang813/clawd-actor</a></b> · ⭐20 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **20**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-12 |

🏷 `animation` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `clawd` · `hooks` · `spinner`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/brianhuang813--clawd-actor/9a863002f9523229.gif" width="100%" alt="BrianHuang813/clawd-actor animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 13 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ivokund/claude-account-rotator">ivokund/claude-account-rotator</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: rotates between your Claude logins as their usage limits fill

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ivokund--claude-account-rotator/7d0a3ac5b2b44e1b.png" width="100%" alt="ivokund/claude-account-rotator screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ivokund--claude-account-rotator/5202f19d431bd1af.gif" width="100%" alt="ivokund/claude-account-rotator animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐15 · TypeScript · 👁️ observed · 13 天</summary>

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
| Stars        | **15**     |
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
<summary>🧩 <b><a href="https://github.com/rashedInt32/glass">rashedInt32/glass</a></b> · ⭐15 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

A desktop-app look for Claude Code's terminal transcript, as a mod

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **15**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `developer-tools` · `markdown` · `syntax-highlighting` · `terminal-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/rashedint32--glass/87a4efdbb6ca206e.png" width="100%" alt="rashedInt32/glass screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **15**     |
| Last push    | 2026-10-13 |
| First listed | 2026-10-13 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unayung--cc-mods-enil/c1156c6f17379207.png" width="100%" alt="Unayung/cc-mods-enil screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 13 天</summary>

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
| Stars        | **14**     |
| Last push    | 2026-10-03 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/jetsonchan--cc-usage-band/e9d74f1543fa7c25.png" width="100%" alt="JetsonChan/CC-Usage-Band screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐13 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **13**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `claude-code-plugins` · `claude-code-statusline`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/5e1358adde3e377d.png" width="100%" alt="augiefra/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/augiefra--claude-mods/27f137c61fc42d0c.gif" width="100%" alt="augiefra/claude-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐13 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **13**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐11 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **11**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-10 |

🏷 `animation` · `ascii-art` · `claude` · `claude-code` · `claude-mods` · `pixel-art` · `plugin` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/a2bacbca880dcd7d.gif" width="100%" alt="furqan-khan07/pixelband screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/furqan-khan07--pixelband/53dd07a5a38530b0.gif" width="100%" alt="furqan-khan07/pixelband animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 6 天</summary>

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
| Stars        | **10**     |
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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mods that keep context use, plan quota and per-turn cost on screen, plus a guard that stops a session once it goes over budget.

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
| Last push    | 2026-10-16 |
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
| Last push    | 2026-10-16 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **9**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Assistir em youtube.com</a> · a reprodução é aberta no site de origem; GitHub não pode incorporá-la em linha</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 433</sub></summary>

- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mods de Claude Code de Ray Amjad: painéis, faixas, proteções de prompt…
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Mods do Claude Code criados por Darrell Wang — faixas acima do prompt, sem…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agentes, comandos, regras, hooks e estilos de saída especializados para…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods do Claude e as ferramentas para criá-los: primeiro uma skill de criação…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatro mods do Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - O harness do Claude Code que uso todos os dias, publicado com este nome desde o…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Troque o telhado do Claude Code usando Claude Mods: sem alterar o binário…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Build, testes, console e prévias do SwiftUI do Xcode dentro do Claude Code.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conhecimento do Obsidian com fontes citadas sobre Claude Code mods…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods do Claude Code do Learning Hacker: transforme o funcionamento do agent em…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods do Claude Code que corrigem e traduzem seus prompts antes que Claude os…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Painel lateral do Claude Desktop (aba Code): lista todos os afazeres inacabados…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso acima da caixa de entrada do Claude Desktop (aba Code): cota de 5h…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods e skills de Claude Code do Nekyia Labs, criados e usados diariamente por…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Um painel lateral para o código Claude: os subagentes executados por uma…
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Um cartão de status flutuante para o Claude Code — modelo, contexto, limites de…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de hooks de função) para Claude Code.
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill que ensina agentes do Claude Code a criar Claude Mods.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Uma fila de decisões CLI/TUI para humanos que trabalham com agentes…
- [michalstrnadel/AgentBar](https://github.com/michalstrnadel/AgentBar) - Approve Claude Code permission prompts right from your menu bar — no terminal…
- [mishgoldenberg/claude-mods](https://github.com/mishgoldenberg/claude-mods) - Painéis, proteções e mods de qualidade de vida para Claude Code: contexto, uso…
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins e skills comunitários do Claude, instaláveis em um único mercado.
- [az9713/claude-mod-pack](https://github.com/az9713/claude-mod-pack) - Seis mods de Claude Code em um único plugin.
- [davekiss/mods](https://github.com/davekiss/mods) - Mods do Claude Code por Dave Kiss.
- [nogu66/md-prompt](https://github.com/nogu66/md-prompt) - Markdown, painted onto Claude Code.
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de código do Claude sob demanda — uma habilidade que lê sua conversa e…
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - A galeria de mods do Baselane: mods de Claude Code, verificados e fixados.
- [Danovich/turntype](https://github.com/Danovich/turntype) - Um teste de digitação para passar o tempo enquanto Claude trabalha.
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Uma loja de aplicativos para mods do Claude Code, dentro do Claude Code: /mods…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: limites do plano e contexto acima do prompt, um…
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) do Claude Code que adiciona um painel lateral com abas Activity…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod do Claude Code que desenha diffs de Edit e Write em duas colunas lado a lado.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods de Claude Code: painel de uso 像素螃蟹 usage-hud + links HTML clicáveis no…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods para o Claude Code: plugins de function-hook que adicionam painéis…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nomes e segredos enquanto você…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods e skins para Claude Code: uma barra de progresso ao vivo para as tarefas…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensões do Claude Code. Desbloqueie todo o poder do Claude.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dois mods de Claude Code para executar muitas sessões simultaneamente: um…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dois mods de Claude Code acima da caixa de prompt: medidor da janela de…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace dos meus mods do Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Leia os arquivos Markdown nomeados pelo código Claude, renderizados ao lado da…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow para Claude Code: uma checklist calma acima do prompt mostrando o…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, painel de agentes, desfoque PDPA.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imagens coladas acima do prompt, em qualquer…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Colega de trabalho por voz para o Claude Code.
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, um velocímetro de digitação ao vivo com…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para o Claude Code: painéis, comandos e hooks criados com o plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubra mods, plugins e extensões de Claude Code com demonstrações animadas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas mermaid desenhados diretamente na transcrição.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequenos mods do Claude Code (plugins de function-hook): session-switcher e mais.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encontre os mods que você mais usaria)…
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de ferramentas de Naren para Claude: skills, mods e servidores MCP para o…
- [nicolas-codemate/claude-code-mods](https://github.com/nicolas-codemate/claude-code-mods) - Mods for Claude Code.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Vários mods do claude code criados por mim.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubra, inspecione, alterne e atualize mods de Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Melhores mods de Claude Code: selecionados, validados e fixados.
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods do Claude Code para Engineers de verdade.
- [Coolkidlab-Yin/agent-mobile-control](https://github.com/Coolkidlab-Yin/agent-mobile-control) - Drive your local Claude Code and Codex sessions from your phone, as chat rooms.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin do Claude Code: roteamento automático de modelos Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascote Clawd animado, barras de limite de uso e…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Cultive um ovo de chá que ganha sabor lentamente enquanto você escreve código ·…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código de código aberto para o Claude Code: painéis, linhas de status…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code: responda a Claude ponto por ponto, diretamente no texto.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
- [oMaN-Rod/claude-code-widgets](https://github.com/oMaN-Rod/claude-code-widgets) - Small cards that sit under the Claude Code prompt, or docked beside the…
- [omeerdvrn/o-mods](https://github.com/omeerdvrn/o-mods)
- [peeratop02/attention-sounds](https://github.com/peeratop02/attention-sounds) - Claude Code mod: plays a sound when Claude is done, needs permission, or asks a…
- [raresmun/claude-mods](https://github.com/raresmun/claude-mods) - Mods para Claude Code: Clawd, um pequeno mascote pixelado que representa o que…
- [reporails/arcade](https://github.com/reporails/arcade) - Jogos clássicos de desktop como mods de Claude Code, jogados em um painel…
- [schreibse/claude-code-mods](https://github.com/schreibse/claude-code-mods) - code-mods para claude.
- [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope) - Um mod do Claude Code que ativa ou desativa suas habilidades, agentes, regras e…
- [Singh-AP/awesome-claude-mods](https://github.com/Singh-AP/awesome-claude-mods) - 🧩 Mods do Claude Code testados e instaláveis com um comando: proteções para o…
- [soulrocha/Claude-code-hero-journey](https://github.com/soulrocha/Claude-code-hero-journey) - 🦀 A cozy RPG HUD mod for Claude Code.
- [testy-cool/awesome-claude-code-mods](https://github.com/testy-cool/awesome-claude-code-mods) - Uma lista selecionada de mods de código do Claude, instaláveis como um…
- [wdsewdser-bit/claude-code-mods](https://github.com/wdsewdser-bit/claude-code-mods) - Dois mods de Claude Code: cache-keeper e ctx-mod.
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantêm um agente honesto — hooks de função que protegem…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Um mod de Claude Code para capturar pensamentos durante o trabalho…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods do Claude Code de Herman (marketplace herman-mods).
- [jrlprost/claude-code-mods](https://github.com/jrlprost/claude-code-mods) - Claude Code mods I build because I need them: context bar, plugin toggler, and…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod: escolhe o modelo e o esforço de raciocínio de cada subagente.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) de Claude Code que faz a interface de terminal do Claude Code…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Veja o que o Claude Code executa em segundo plano: subagentes, tarefas de…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo do primeiro dia sobre mods do Claude Code no Windows: uma barra…
- [MichaelP17/claude-mods](https://github.com/MichaelP17/claude-mods) - Mods I made and personally use in my Claude Code setup.
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [partalemre/MODZ](https://github.com/partalemre/MODZ) - 17 Claude Code plugins in one panel. See every move Claude makes: agents…
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod do Claude Code: medidores ao vivo de custo, contexto e cota do plano acima…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod do Claude Code: um SDLC nativo de IA.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Dê uma palmada em Claude quando ele fizer besteira — um mod de alívio de…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, com comprovantes. Um plugin que planeja, delega e comprova que o…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar and a status line for Claude Code: usage limits, context, model…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprenda um idioma estrangeiro enquanto trabalha com o código Claude.
- [AJMarquez99/prompt-pin](https://github.com/AJMarquez99/prompt-pin) - Pin your latest prompt above the input and browse this session.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de custos, tokens e uso de contexto em tempo real para Claude…
- [atozzi-dev/model-escalator](https://github.com/atozzi-dev/model-escalator) - Claude Code mod that runs cheap models in parallel and escalates to a stronger…
- [CircularBlox/Clarity](https://github.com/CircularBlox/Clarity) - A clearer Claude Code terminal: boxed and organized you/claude conversations…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Um mod do Claude Code que mantém uma lista atualizada dos itens em aberto em…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Veja quais arquivos cada agente do Claude Code tem em seu contexto, e quanto de…
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequenos mods do Claude Code para o terminal e o aplicativo desktop.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidade + mod Claude CLI que adiciona palavras em espanhol às respostas do…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Seu backlog Floatee acima do prompt do Claude Code: execute, guie e marque seus…
- [funkadelic/claude-secret-scrub](https://github.com/funkadelic/claude-secret-scrub)
- [gabriel9004/claude-code-mods](https://github.com/gabriel9004/claude-code-mods) - Mods para Claude Code: panel de agentes y tareas con cuota y caché, y banda de…
- [heyJordanParker/cmod](https://github.com/heyJordanParker/cmod) - Claude Mod Manager: install, try, build, check, and publish Claude Code mods.
- [intent-driven-dev/claude-mods](https://github.com/intent-driven-dev/claude-mods) - Claude Code mods: live panes and hooks for everyday workflows.
- [iuliandita/mods](https://github.com/iuliandita/mods) - Claude Code mods you can install one at a time.
- [JimmySadek/claude-code-tint-mod](https://github.com/JimmySadek/claude-code-tint-mod) - Claude Code mod (CC tint mod): color each window by its repository, ring the…
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - A janela de contexto como uma linha acima do prompt, desenhada da forma como o…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Não deixe sua atenção se dispersar enquanto espera pela resposta do Claude Code.
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Um plugin gratuito e de código aberto para Claude Code.
- [magiccreator-ai/awesome-claude-code-mods](https://github.com/magiccreator-ai/awesome-claude-code-mods) - Curated Claude Code mods, original creator demos, public repositories, and…
- [markfulton/safe-keys](https://github.com/markfulton/safe-keys) - Paste an API key into Claude Code. Nothing keeps it.
- [meganemura/pull-request-pane](https://github.com/meganemura/pull-request-pane) - A Claude Mod that shows the session.
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [nninkovic95/clawd-band](https://github.com/nninkovic95/clawd-band) - Animated Clawd + weekly/5-hour usage bars and reset countdowns above the Claude…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Skills do Claude Code: verificador de fatos para documentos, auditor de código…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Painel lateral ao vivo de estatísticas da sessão para a aba Code do aplicativo…
- [qizhuxu/qi-pm](https://github.com/qizhuxu/qi-pm) - Claude Code mod: rewrite the prompt-box draft with a side model call, then put…
- [RemyLespagnol/sharp-compact](https://github.com/RemyLespagnol/sharp-compact) - Claude Code mod: before every compaction, the session writes its own handoff…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: um mod de Claude Code que lê em voz alta as respostas de Claude e…
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods do Claude Code: pequenos plugins para painéis ao vivo, roteamento de…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin do Claude Code: monitor de uso, rastreador de tokens e linha de…
- [verdantran/code-city](https://github.com/verdantran/code-city) - An idle pixel-art city for Claude Code.
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mods do Claude Code: EMCC (Every Mod Claude Code), uma coleção selecionada e…
- [XyndoX/repograph](https://github.com/XyndoX/repograph) - Obsidian-style repo graph pane for Claude Code: files, dependencies and changes…
- [zchee/claude-code-mods](https://github.com/zchee/claude-code-mods)
- [a-pavithraa/claude-mods](https://github.com/a-pavithraa/claude-mods)
- [Abdoul-sudo/prompt-enhancer](https://github.com/Abdoul-sudo/prompt-enhancer) - Claude Code mod: rewrites vague prompts using the active project.
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Um gato de braille animado acima do prompt do Claude Code.
- [allanvigiani/claude-mods](https://github.com/allanvigiani/claude-mods)
- [allorders1studio/claude-code-mods](https://github.com/allorders1studio/claude-code-mods) - Claude Code mods: Dokploy deploy status bar, Git worktree overview, Message-Hub…
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Um gato em pixel acima do seu prompt do Claude Code que executa uma chamada de…
- [alvaro-hi/progress-ring](https://github.com/alvaro-hi/progress-ring) - Progress Ring for Claude Code: know where Claude is in a long plan.
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Um mod do Claude Code que escolhe um bom momento para compactar e manter…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods Claude para o Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de uso geral para o Claude Code: faixas, painéis, toasts e hooks.
- [androidZzT/cc-moyu-kit](https://github.com/androidZzT/cc-moyu-kit) - Claude Code mods for watching the market from the terminal: A股/港股/美股 pane with…
- [Anerco/claude-code-flappy-claude](https://github.com/Anerco/claude-code-flappy-claude) - Claude Code mod: Flappy Bird with Claude.
- [arjunkambj/claude-mods](https://github.com/arjunkambj/claude-mods) - Arjun.
- [Arkboi-GG/claude-mods](https://github.com/Arkboi-GG/claude-mods) - A small collection of Claude Code mods.
- [arthurglaizal/quiet-token-bar](https://github.com/arthurglaizal/quiet-token-bar) - A Claude Code mod: your context window in one quiet line, grey until it matters.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Seus limites de uso do Claude como um cartão de saúde de aldeão animado, com um…
- [AskTinNguyen/ather-mods](https://github.com/AskTinNguyen/ather-mods) - Claude Code mods for the S2 team (the ather marketplace).
- [astromelon/takgon-mods](https://github.com/astromelon/takgon-mods) - 개인 Claude Code mods 플러그인(takgon-mods).
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Treinos curtos enquanto Claude trabalha: uma meta diária, sequências…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [AydinHassan/claude-mods](https://github.com/AydinHassan/claude-mods) - Claude Code mods.
- [bardaxx/modsbook](https://github.com/bardaxx/modsbook) - A book of Claude Code mods: side panes, bands, status lines and hooks, each one…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para o código Claude: Apple Music e Spotify acima do prompt…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [blackironj/claude-mods](https://github.com/blackironj/claude-mods)
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [brianjmeier/claude-codemode](https://github.com/brianjmeier/claude-codemode) - Claude Code mod: one JavaScript program over Claude Code.
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: relógio de cache, raio de impacto, sugestões, lista de…
- [Broo37/claude-mods](https://github.com/Broo37/claude-mods) - Mods for Claude Code: Clean View hides tool calls and shows the plan as a…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Apenas uma coruja para o seu Claude Code.
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [comdoly-life/claude-session-dashboard](https://github.com/comdoly-life/claude-session-dashboard) - Claude Code mod: live dashboard of subagents, agent teams and workflows with…
- [DamianoSrb/Mods](https://github.com/DamianoSrb/Mods) - Claude code mods.
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [davidyerm/claude-mods](https://github.com/davidyerm/claude-mods) - Mods for Claude Code.
- [DazzleML/claude-bookmarks](https://github.com/DazzleML/claude-bookmarks) - Bookmarks and vim-style marks inside Claude Code terminal conversations…
- [diegocamara89/claude-mods](https://github.com/diegocamara89/claude-mods) - Mods do Claude Code (function hooks): Sonnet por padrão para subagentes…
- [Djdhmf/clawd-office](https://github.com/Djdhmf/clawd-office) - A Claude Code mod: a living 8-bit office of Claude crabs in a side panel that…
- [Djdhmf/prompt-enhancer](https://github.com/Djdhmf/prompt-enhancer) - A Claude Code mod: a pixel-art librarian crab above your prompt that rewrites…
- [drprockz/claude-mods](https://github.com/drprockz/claude-mods) - Private Claude Code mods (marketplace: drprockz-mods).
- [dtakamiya/claude-code-mods](https://github.com/dtakamiya/claude-code-mods) - Claude Code Mods marketplace.
- [edsoncantuaria/cc-cost](https://github.com/edsoncantuaria/cc-cost) - Claude Code mod: live token usage vs your 5h/7d subscription limits.
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [EslamHanafy/delegate-watch](https://github.com/EslamHanafy/delegate-watch) - Live Claude Code pane that shows what your delegated coding agents.
- [estevanhernandez-stack-ed/sanduhr-mods](https://github.com/estevanhernandez-stack-ed/sanduhr-mods) - Claude Code mods, published from Sanduhr.
- [exsec-dev/skills-used](https://github.com/exsec-dev/skills-used) - A Claude Code mod that shows which skills Claude used in the session.
- [feizaodemon/claude-mods](https://github.com/feizaodemon/claude-mods) - Claude Code mods (function-hook plugins): session-meter and more.
- [FunJim/claude-code-add-to-chat](https://github.com/FunJim/claude-code-add-to-chat) - Codex-style Add to chat for Claude Code: annotate any part of a reply, send all…
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [grvermeulen/claude-mods](https://github.com/grvermeulen/claude-mods) - Claude Code mods: tweaked copies of community mods.
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by gwarf: a plugin marketplace.
- [gyoomun/claude-mods](https://github.com/gyoomun/claude-mods) - 다른 사람이 만든 Claude Code 모드를 내 작업 방식에 맞게 고친 것 (coach-on-call, next-steps-multi).
- [hal-9/claude-mods](https://github.com/hal-9/claude-mods) - Private marketplace of Claude Code mods.
- [hearsawho25/roberts-mods](https://github.com/hearsawho25/roberts-mods) - Claude Code mods (hooks-module plugins) shared as a plugin marketplace. MIT.
- [hicrandn/claude-mods](https://github.com/hicrandn/claude-mods) - Claude Code mods marketplace (hicran-mods).
- [HikiJun97/claude-mods](https://github.com/HikiJun97/claude-mods) - Personal Claude Code mods.
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [hyperbola-bear/claude-mods](https://github.com/hyperbola-bear/claude-mods) - for my claude mods.
- [ijat/prompt-polish](https://github.com/ijat/prompt-polish) - Claude Code mod that cleans up voice-dictated prompts and teaches the fix.
- [Ilja-Garbuz/claude-code-mods](https://github.com/Ilja-Garbuz/claude-code-mods) - Claude Code terminal mods: session side panel, opencode-style prompt panels…
- [jambolo/claude-mods](https://github.com/jambolo/claude-mods) - Mods for Claude Code.
- [jaylane/doorbell](https://github.com/jaylane/doorbell) - Claude Code mod: GitHub PR review requests, comments, approvals and releases on…
- [jaylane/pilot-light](https://github.com/jaylane/pilot-light) - Keeps your Claude Code prompt cache warm, and shows what your session is…
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Painel de uso do contexto na barra lateral: total, categorias, crescimento por…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista de arquivos na barra lateral: quais arquivos foram criados, modificados…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, um coelho holandês anão preto e branco em estilo 8-bit, corre e pula acima…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - A seção “O que eu perguntei” na barra lateral: cada frase que o usuário digitou…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linha do tempo na barra lateral: onde o tempo desta rodada foi gasto.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Movimentação de tokens na barra lateral: quantos tokens a conversa principal…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - O “confessionário honesto” do claude code: após responder em cada rodada…
- [jonirafael/claude-code-mods](https://github.com/jonirafael/claude-code-mods) - Claude Code mods: context-receipt (per-turn context breakdown) and…
- [jorgehsy/claude-mods](https://github.com/jorgehsy/claude-mods) - Catálogo de mods para Claude Code.
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Know the question before it is asked, and what you can safely say.
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive em uma faixa acima do prompt do Claude Code: encena a sessão, mostra…
- [kaisudo0520/cc-dashboard](https://github.com/kaisudo0520/cc-dashboard) - Live mission-control pane for Claude Code: Fable and Codex usage, branch review…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Um mod que lê em voz alta as respostas e notificações do Claude Code usando…
- [keisato848/claude-mods](https://github.com/keisato848/claude-mods)
- [kelokchan/optimize-prompt](https://github.com/kelokchan/optimize-prompt) - Claude Code mod: Optimize prompt button, Haiku rewrites your draft in place.
- [KingP1197/claude-mods](https://github.com/KingP1197/claude-mods) - Niceties/quality of life improvement Claude mods.
- [Krishna30396/Pixel-Progress](https://github.com/Krishna30396/Pixel-Progress) - A pixel progress bar with time left for Claude Code: tasks done, percent and…
- [KytioisaCat/playpen](https://github.com/KytioisaCat/playpen) - Who needs attention? Your other Claude Code sessions as cards above the prompt…
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [luismiggarcia/claude-usage-bars](https://github.com/luismiggarcia/claude-usage-bars) - Claude Code mod: barras de contexto, sessão (5h) e semana acima do prompt.
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Um mod do Claude Code que mostra o que Claude está fazendo no subtítulo da aba…
- [makingaipractical/brain-drain-for-claude-code](https://github.com/makingaipractical/brain-drain-for-claude-code) - How full Claude.
- [malinfossum/mango-buddy](https://github.com/malinfossum/mango-buddy) - A fluffy black cat above your Claude Code prompt.
- [Marceux-Croix/Claudeopticon](https://github.com/Marceux-Croix/Claudeopticon) - A process monitoring and ticket system for Claude Code: your todo as a live…
- [MDmubarak786/claude-mods](https://github.com/MDmubarak786/claude-mods) - Community mods for Claude Code: guards, panes, and commands that run inside…
- [michaelSelbertinger/payback](https://github.com/michaelSelbertinger/payback) - Payback is a Claude Code mod that counts what Claude finished for you, sorts…
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [moabualruz/rice-multi-models](https://github.com/moabualruz/rice-multi-models) - Claude Code mod: Codex (ChatGPT subscription) and other non-Anthropic models as…
- [mreedr/gh-linear-parse-mod](https://github.com/mreedr/gh-linear-parse-mod) - Claude Code mod: GitHub PR and Linear links band above the prompt.
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod do Claude Code que reativa as ferramentas de tarefas pendentes para modelos…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod do Claude Code que espera uma pausa segura e então transfere sua sessão ou…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod do Claude Code: uma linha por tarefa acima do prompt com a tarefa atual…
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jogue Connect Four contra uma AI dentro do Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: quando outro agente de programação faz commit no seu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositórios compartilhados por vários agentes de IA…
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [nxhung1610/claude-odometer](https://github.com/nxhung1610/claude-odometer) - Claude Code mod that shows your 5-hour and 7-day usage limits right under the…
- [OG-Matcha/tessera](https://github.com/OG-Matcha/tessera) - One mod for Claude Code, Windows and CJK first: pasted-image and text previews…
- [OlivierAlter/prompt-coach](https://github.com/OlivierAlter/prompt-coach) - Claude Code mod: reviews your prompts, tracks your prompting habits, and…
- [OskarasM/workbar](https://github.com/OskarasM/workbar) - Claude Code mod: live progress with honest time estimates, subagent rows, chat…
- [pappusinghadip/pappu-claude-mods](https://github.com/pappusinghadip/pappu-claude-mods)
- [Paradox07127/claude-utopia](https://github.com/Paradox07127/claude-utopia) - Claude Code mods with agent telemetry, timeline dashboards, mmrun cross-model…
- [partalemre/transceiver](https://github.com/partalemre/transceiver) - Claude Code plugin (beta): team chat inside Claude Code.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: um Claude Code mod. Worktrees permanentes com início somente…
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [petrovyuri/claude-code-mods](https://github.com/petrovyuri/claude-code-mods)
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [PinkOctopusLabs/claude-simple-usage](https://github.com/PinkOctopusLabs/claude-simple-usage) - Claude Code mod showing context-window and rate-limit usage under the prompt.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pvjbuilds/crab-buddy](https://github.com/pvjbuilds/crab-buddy) - An animated pixel-art Claude crab for Claude Code: it acts out what Claude is…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [r1305/claude-mods](https://github.com/r1305/claude-mods) - Mods para Claude Code: enrutado de modelos con dashboard de consumo y…
- [ramtinJ95/claude-mods](https://github.com/ramtinJ95/claude-mods) - Claude Code mods, published as one plugin marketplace.
- [raoofaltaher/claude-code-mods](https://github.com/raoofaltaher/claude-code-mods) - Claude Code mods: account-bars (live session/weekly limit bars per account) and…
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod do Claude Code: flexões para fazer enquanto Claude trabalha. Sem tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: um guia de campo para Claude Code mods, de ELI5 a engenharia de…
- [roboza/kanbot](https://github.com/roboza/kanbot) - A global kanban board in Claude Code that hands queued cards to background…
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [ryx2/slopshopper](https://github.com/ryx2/slopshopper) - The mod shop for Claude Code: scrapes GitHub for mods, previews them, hosts a…
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod do Claude Code: transforma o plano que você aprova no modo de planejamento…
- [sabasayer/crew](https://github.com/sabasayer/crew) - Claude Code mod: live board of /crew agent progress.
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Uma lista selecionada de mods do Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sem custo: os agentes auxiliares rodam no Haiku, e arquivos grandes e logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Uma trilha sonora lofi que acompanha a sessão: calma, foco, fluxo, além de…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprenda enquanto Claude programa: após um turno que alterou o código, uma…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Uma gravação de cada edição feita por Claude: reproduza cada alteração sendo…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [SashimmyUni/polis](https://github.com/SashimmyUni/polis) - A Claude Code mod: a project dashboard and isometric city map of tasks, agents…
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [shou6/claude-mods](https://github.com/shou6/claude-mods)
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [sourabp/claude-session-bar](https://github.com/sourabp/claude-session-bar) - Claude Code mod: a band above the prompt showing your starship prompt.
- [sr-gene/gene-claude-mods](https://github.com/sr-gene/gene-claude-mods)
- [srwiseman/claude-mods](https://github.com/srwiseman/claude-mods)
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [StarHawkMK1/cc-mods](https://github.com/StarHawkMK1/cc-mods) - Custom Claude Code mods marketplace (cc-mods), with vendored Anthropic sample…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensagens de commit com um clique para Claude Code com uma Malenia dançante em…
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — uma modificação do Claude Code que mostra o uso do seu plano…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mods não oficiais do Claude Code por tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Um mod do Claude Code que mostra a sessão atual em um painel: cada prompt, o…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Um marketplace de plugins do Claude Code de mods: plugins function-hooks que…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [thomthom/claude-usage-line](https://github.com/thomthom/claude-usage-line) - Claude Code mod: context, session and weekly usage as rings above the message…
- [timoranjes/agent-arcade](https://github.com/timoranjes/agent-arcade) - Playful live view of Claude and its subagents: animated dashboard, stats band…
- [tinkybeatz/tinky-claude-mods](https://github.com/tinkybeatz/tinky-claude-mods) - Claude Code mods: interface and behaviour plugins built on function hooks.
- [ttqteo/claude-skim](https://github.com/ttqteo/claude-skim) - A Claude Code mod that highlights the 2-4 sentences of a long reply you…
- [tyler4400/tyler-claude-mods](https://github.com/tyler4400/tyler-claude-mods) - Claude Code plugins: status-card (会话状态卡片) &amp; session-title (智能自动标题) — Live…
- [user0027/claude-mods](https://github.com/user0027/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod do Claude Code: faixa de progresso animada e resumo de conclusão para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Três pequenos mods de Claude Code: veja quando seus subagentes terminarão…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Diga &quot;Estou perdido&quot; e Claude explicará novamente sua última resposta em…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Faça uma pergunta paralela a Claude em um painel ao lado do seu trabalho.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vmlinuz82/claude-mods](https://github.com/vmlinuz82/claude-mods) - Claude Code mods: a task checklist and a skill/MCP usage band, for the terminal…
- [WBLD4A/pr-radar](https://github.com/WBLD4A/pr-radar) - Claude Code mod: a pane of your GitHub pull requests sorted by who must act.
- [williamchong/cc-mod-caffeinate](https://github.com/williamchong/cc-mod-caffeinate) - A Claude Code mod that keeps your Mac.
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wonjangcloud9/wj-mods](https://github.com/wonjangcloud9/wj-mods) - Claude Code mods: cross-session work progress pane, usage band, long-turn…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin do Claude Code: seus limites de uso do Claude Pro/Max com previsão de…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para o Claude Code. agent-crew: acompanhe seus subagentes trabalhando como…
- [XyndoX/agentdeck](https://github.com/XyndoX/agentdeck) - A live AI-agent dashboard in a Claude Code pane: agent flow, tool activity…
- [ya8282/claude-code-mods](https://github.com/ya8282/claude-code-mods) - Small productivity mods for Claude Code.
- [Yumbang/scopus-for-dobby](https://github.com/Yumbang/scopus-for-dobby) - Stateful CLI for searching, collecting, and managing academic papers from the…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - Uma coleção selecionada a dedo dos melhores recursos para os agentes mais…
- [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) - Um plugin do Claude Code que mostra o que está acontecendo — uso de contexto…
- [sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline) - 🚀 Linha de status bonita e altamente personalizável para Claude Code CLI, com…
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Todas as partes do prompt de sistema do Claude Code, 27 descrições de…
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - Skill de vídeo com IA para Claude Code e Codex — vídeos cinematográficos de…
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - Mais de 45 dicas para aproveitar ao máximo o Claude Code, do básico ao avançado…
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - 🪧 Claude Code / habilidade Codex — gere carrosséis para Xiaohongshu e pares de…
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - A terminal window manager that knows what your agents are doing.
- [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) - Revise o diff do seu agente de programação em um painel do terminal e envie…
- [uppinote20/claude-dashboard](https://github.com/uppinote20/claude-dashboard) - Plugin abrangente de linha de status para o Claude Code, com uso de contexto…
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Crie mods para Claude Code: conecte qualquer solicitação, modifique qualquer…
- [aqua5230/usage](https://github.com/aqua5230/usage) - macOS menu bar &amp; Windows tray app pinning Claude Code, Codex, Antigravity &amp;…
- [NYCU-Chung/cc-statusline](https://github.com/NYCU-Chung/cc-statusline) - Um painel abrangente de statusline para Claude Code — informações da sessão…
- [tmck-code/yet-another-statusline](https://github.com/tmck-code/yet-another-statusline) - A statusline for Claude Code inspired by terminal monitor programs.
- [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) - claude-carbon: acompanhe a pegada de carbono das suas sessões do Claude Code.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mods públicos para Claude Code.
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) - DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash e guias para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs e agentes de programação gratuitos e legais — atualizados…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill que transforma seu agente de programação em especialista em…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horários de oração, data Hijri, adhkar, ayah diária, jejum sunnah, Ramadan…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [WaterTian/cc-hud](https://github.com/WaterTian/cc-hud) - Compact Claude Code statusline — zero-dependency, crash-free on Windows.
- [benz-ai-x/dsh-research-graph](https://github.com/benz-ai-x/dsh-research-graph) - DSH Research Graph · 研图 — DeepSeek Harness plugin for research topics…
- [romacv/claude-plan-usage-statusline](https://github.com/romacv/claude-plan-usage-statusline) - Claude Code status line showing model, usage limits, git info, and workspace…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Coleção de plugins para Claude Code, pi e DeepSeek Harness: HUD da barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de ferramentas portátil do Claude Code para DDD/Arquitetura Limpa em .NET…
- [axlaser/pitwall](https://github.com/axlaser/pitwall) - A rich, color-coded custom statusline for Claude Code showing context usage…
- [3xDevOps/aether](https://github.com/3xDevOps/aether) - Self-hosted multiplayer cloud runtime for coding agents.
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuração global portátil do Claude Code: habilidades personalizadas, hooks…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods não oficiais para a aba Code do Claude Desktop — usage-pet: uma faixa de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins do Claude Code que uso todos os dias: skills e mods, organizados para…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Uma linha de status personalizável para Claude Code com um editor de arrastar e…
- [ogxo-io/plugins](https://github.com/ogxo-io/plugins) - Claude Code plugin marketplace from ogxo: cost-aware agent routing with a live…
- [Shakibuzzaman3104/claude-hydra](https://github.com/Shakibuzzaman3104/claude-hydra) - Hydra: Claude Code dev mod where Claude leads and Command Code heads implement…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins e skills do Claude Code para facilitar mods do jogo…
- [frsorrentino/fable-director](https://github.com/frsorrentino/fable-director) - Token governance for Claude Code: the top model directs, execution goes to the…
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizador de painéis divididos para o Claude Code no Windows Terminal e…
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositório de mods Awesome Media para Claude Code.
- [dayfinggg/anthropic-claude-code-agent-skills](https://github.com/dayfinggg/anthropic-claude-code-agent-skills) - 18 engineering skills, 14 specialist agents, the Brief output style, two mods…
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [michalschroeder/claude-statusline](https://github.com/michalschroeder/claude-statusline) - My Claude Code statusline + supporting hooks.
- [OFurtun/claude-custom-statusline](https://github.com/OFurtun/claude-custom-statusline) - Furtun.
- [RaggioS/claude-code-statusline](https://github.com/RaggioS/claude-code-statusline) - Single-file POSIX statusline for Claude Code: dir, git branch, model, context…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [aquahitt/claude-code-limit-alerts](https://github.com/aquahitt/claude-code-limit-alerts) - Usage-limit alerts for Claude Code: macOS notifications, in-app warnings and…
- [faleiro-thiago/claude-skills-mods](https://github.com/faleiro-thiago/claude-skills-mods) - Facilitadores pessoais para Claude Code, versionados por item.
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [okanerturan/claude-statusblocks](https://github.com/okanerturan/claude-statusblocks) - Adaptive, block-based status line for Claude Code with bin-packing layout.
- [yedidya-buildfy/claude-addons](https://github.com/yedidya-buildfy/claude-addons) - Claude Code add-ons: tab-status colored dot watcher + bundled GSD statusline.
- [afarrell/claude-meter](https://github.com/afarrell/claude-meter) - Minimal Claude Code statusline — context bar, 5h bar, and 7-day rolling…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline do Claude Code de nível profissional: duração da sessão, custo em…
- [duplonicus/claude-statusline](https://github.com/duplonicus/claude-statusline) - Two-row status line for Claude Code: context, rate limits with pace markers…
- [federbenjamin/claude-statusline](https://github.com/federbenjamin/claude-statusline) - A two-line Claude Code status line showing branch, PR, model, context, cost…
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [Happykiller/claude-chat-roles](https://github.com/Happykiller/claude-chat-roles) - Mod Claude Code : barre de couleur, étiquette et heure sur chaque message du…
- [hey-yvan/claude-quota-bar](https://github.com/hey-yvan/claude-quota-bar) - Fast Rust statusline for Claude Code — battery-bar 5h/7d quota, ctx, cache age…
- [itamartz/ClaudeCode-Mods](https://github.com/itamartz/ClaudeCode-Mods) - A Claude Code plugin marketplace of personal mods: hooks, panes and commands…
- [jinhuang712/claude-super-statusline](https://github.com/jinhuang712/claude-super-statusline) - A SUPER customizable &amp; pretty statusline for Claude — in Claude Code and the…
- [Jul879n/claude-pets](https://github.com/Jul879n/claude-pets) - Mod &#x27;mascotas&#x27; para Claude Code: mascotas de pixel art que muestran qué hacen…
- [julien-m/claude-statusline](https://github.com/julien-m/claude-statusline) - Modular Claude Code statusline showing Git state, context, usage and session…
- [LemonYangZW/cc-mods](https://github.com/LemonYangZW/cc-mods) - Practical, low-distraction mods for Claude Code.
- [LiamMorganDev/claude-setup](https://github.com/LiamMorganDev/claude-setup) - My complete Claude Code setup: mods, skills, commands, hooks and CLAUDE.md…
- [LucasXCoder/noetra-claude-setup](https://github.com/LucasXCoder/noetra-claude-setup) - Tuned Claude Code setup: mandatory verify-before-done workflow, 84 skills, 33…
- [luck7x/claude-cache-keepalive](https://github.com/luck7x/claude-cache-keepalive) - Keep Claude Code&#x27;s prompt cache warm while you&#x27;re away — cheap…
- [Maggi-Controls-S-R-L/claude-statusline](https://github.com/Maggi-Controls-S-R-L/claude-statusline) - A compact two-line status line for Claude Code.
- [matthewjschultz/claude-statusline](https://github.com/matthewjschultz/claude-statusline) - Custom Claude Code status line with context window, API usage tracking, git…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [n0nuser/claude-statusline](https://github.com/n0nuser/claude-statusline) - 3-line status bar for Claude Code — model, context usage, cost, git status, and…
- [Nader-mech/claude-statusline](https://github.com/Nader-mech/claude-statusline) - Two-line Claude Code status line: context window, 5-hour and weekly limits with…
- [nhooey/claude-code-usage-statusline](https://github.com/nhooey/claude-code-usage-statusline) - A Claude Code status line and per-turn cost readout in one program: token…
- [ppezzull/glm-claude-hud](https://github.com/ppezzull/glm-claude-hud) - Show GLM Coding Plan (Z.ai/Zhipu) token usage in the claude-hud statusline for…
- [Recokioshi/claude-kit](https://github.com/Recokioshi/claude-kit) - a set of useful skills and mods for claude code.
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Linha de status personalizada do Claude Code.
- [SACRVM/claude-code-statusline](https://github.com/SACRVM/claude-code-statusline) - A Claude Code status line with real Anthropic usage % (5h + 7d), context bar…
- [salaesp/claude-dashboard-mod](https://github.com/salaesp/claude-dashboard-mod) - Dashboard mod for Claude Code: context, goals, agents and what needs you, above…
- [satoramoto/awesome-claude](https://github.com/satoramoto/awesome-claude) - Claude Code config and mods, with a shared component kit, a playground and…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [TheGnarCo/claude-statusline](https://github.com/TheGnarCo/claude-statusline) - The Gnar Company.
- [tichara1/ai.claude-status-panel](https://github.com/tichara1/ai.claude-status-panel) - Mod pro Claude Code: panel nad promptem s kontextem, limity, cenou, stavem…
- [tsalkin/claude-code-statusline](https://github.com/tsalkin/claude-code-statusline) - Two-line status line for Claude Code: context, cache health, effort drift…
- [u007/claude-plugins](https://github.com/u007/claude-plugins) - Personal Claude Code plugin marketplace: context-status statusline and…
- [warodan/vscode-claude-code-patch](https://github.com/warodan/vscode-claude-code-patch) - Claude Code skill (VS Code, Windows): image previews and open buttons under…
- [yacb2/claude-statusline](https://github.com/yacb2/claude-statusline) - Three-line Claude Code status line: context depth, cross-session rate limits…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de deterioração de contexto 2026 — Monitor proativo de memória de IA e…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes e linhas de status do Claude Code: coleções e ferramentas de…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: painéis, faixas e companheiros baseados em hooks de…
- [ryanclark/statusline](https://github.com/ryanclark/statusline) - Simple status line for Claude Code showing context window/usage limits.
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passe tarefas entre suas sessões do Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encontre o que você pede ao Claude Code repetidamente e transforme…
- [devnix/burnbar](https://github.com/devnix/burnbar) - Rich statusline plugin for Claude Code — context window progress bar, token…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Isto em um servidor MCP para controlar o MODS, a ferramenta modular…
- [inematds/skillmanager3x](https://github.com/inematds/skillmanager3x) - Biblioteca de 3 skills para Claude Code: session-handoff, session-statusline e…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex e Claude Code para traduzir mods de CK3 com um LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código aberto e outras extensões para Claude Code.
- [Grandullon/diariovida-mods](https://github.com/Grandullon/diariovida-mods) - Mods gratis para Claude Code: entiende lo que hace Claude, mejora tus prompts y…
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.

</details>

<a id="dsh-cordis"></a>

## Ecossistemas de plugins do DSH e do Cordis

DeepSeek Harness e Cordis chegam ao mesmo lugar por uma direção diferente: para eles, o plugin é o mecanismo de modificação; portanto, um plugin lá equivale a um mod aqui.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐251036 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

DeepSeek Harness: Everything is a Plugin.

<sub>🔧 Encontrado em uso no código: `packages/experimental/claude-code-mods/src/elements.ts`, `packages/experimental/claude-code-mods/src/matcher.ts`, `packages/experimental/claude-code-mods/src/index.ts`, `docs/config-catalog.zh.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                          |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **251036** |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐75482 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **75482**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4670 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

O plugin TUI oficialmente mais recomendado do DSH — alto desempenho, baixo consumo, uma simpática baleia pixelada e interação fluida com o mouse. Instalação com um comando via npm. / Plugin TUI oficialmente mais recomendado pelo DSH, alto desempenho e baixo consumo, simpática baleia pixelada, interação fluida com o mouse, instalação com um comando via npm

<sub>🔧 Encontrado em uso no código: `scripts/verify-kernel-commands.tsx`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                          |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4670**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ccch1mneyyy--dsh-tui/18fd45f8f1eaca04.png" width="100%" alt="ccch1mneyyy/dsh-TUI screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐734 · Python · 👁️ observed · 0 天</summary>

##### 📝 Summary

Uma lista selecionada dos melhores plugins incríveis de IA para assistentes de IA, incluindo Claude Code, OpenAI Codex / ChatGPT, Gemini, Antigravity, Pi / Oh My Pi, Grok, OpenCodek DSH, Kimi e muito mais. https://hol.org/plugins

<sub>🔧 Encontrado em uso no código: `README.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                          |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | Python                                                                |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **734**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐285772 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **285772** |
| Last push    | 2026-10-16 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐84365 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **84365**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/80b6efa0c1ca677d.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35818 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35818**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐31084 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **31084**  |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25687 · Python · 🔎 inferred · 3 天</summary>

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
| Stars        | **25687**  |
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
<summary>🧵 <b><a href="https://github.com/cordiverse/cordis">cordiverse/cordis</a></b> · ⭐9211 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **9211**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-13 |

🏷 `effect` · `framework` · `nodejs` · `plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8825 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8825**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Q00/ouroboros">Q00/ouroboros</a></b> · ⭐6233 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server, 14 runtimes: Claude Code, Codex CLI, Gemini CLI, OpenCode, Copilot, Kiro and more.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **6233**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-os` · `agentic-ai` · `ai-agent` · `ai-coding-agent` · `claude-code` · `cli` · `codex` · `coding-agent`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/5b0b313f6f066fb8.png" width="100%" alt="Q00/ouroboros screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/q00--ouroboros/099492564830e817.gif" width="100%" alt="Q00/ouroboros animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/dsh-tauri/deepseek-harness-desktop">dsh-tauri/deepseek-harness-desktop</a></b> · ⭐3084 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset plugins, Windows / macOS / Linux.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3084**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-desktop` · `dsh-plugin` · `tauri`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/dsh-tauri--deepseek-harness-desktop/f281725e73da1059.png" width="100%" alt="dsh-tauri/deepseek-harness-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/T-Auto/dsh-ops">T-Auto/dsh-ops</a></b> · ⭐2524 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

A toolkit for low-level operations in DSH, designed to reduce token usage and task execution time / DSH 底层操作工具插件，旨在减少 Token 消耗与任务耗时

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2524**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://github.com/T-Auto.png?size=160" width="100%" alt="T-Auto/dsh-ops screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/bowenliang123/dsh-context">bowenliang123/dsh-context</a></b> · ⭐2195 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The best DeepSeek Harness plugin for context insight and management, with context dashboard / browser / sidebar and context command, for context statistics, composition, breakdown, evolution details, agent teams, understanding how the context is made of, and how it evolves. 一站式 DeepSeek Harness 上下文可视化插件，Context 面板、浏览器、侧栏、命令，透视上下文组成、演进、压缩、多 Agent等。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **2195**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cordis-plugin` · `deepseek-harness` · `deepseek-harness-plugin` · `dsh-external` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/bowenliang123--dsh-context/573c0e5849eea852.png" width="100%" alt="bowenliang123/dsh-context screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1219 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Coding agent memory for Claude Code, Codex, Cursor and 39 more, built from the session history already on your disk. Local search, MCP and hooks, no LLM, one Go binary.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Go                                                                                     |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1219**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ysr666/dsh-vision-router">ysr666/dsh-vision-router</a></b> · ⭐1153 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key) + pixel-level vision tools (Q&A, grounding, crop, pixel diff, colors, OCR, SVG trace, cutout, screenshots). One-command install, no Python, image turns work like ordinary tool-calling turns.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1153**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `deepseek-harness` · `dsh` · `dsh-plugin` · `multimodal` · `vision`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/106ad9ed68079834.png" width="100%" alt="ysr666/dsh-vision-router screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ysr666--dsh-vision-router/d79f0c95491a7bc3.gif" width="100%" alt="ysr666/dsh-vision-router animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/TencentCloudBase/CloudBase-AI-Toolkit">TencentCloudBase/CloudBase-AI-Toolkit</a></b> · ⭐1138 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Backend for AI coding agents on CloudBase — database, auth, functions via Plugin, Skills & MCP.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **1138**   |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-skills` · `ai` · `aicoding` · `claude-code` · `cloudbase` · `cursor` · `database` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tencentcloudbase--cloudbase-ai-toolkit/9b9897d8b439ac14.png" width="100%" alt="TencentCloudBase/CloudBase-AI-Toolkit screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ikalus1988/MisakaNet">Ikalus1988/MisakaNet</a></b> · ⭐527 · Python · 🔎 inferred · 0 天</summary>

##### 📝 Summary

📚 Uma biblioteca de microlessons para AI Agents, sem dependências e respaldada por git, para compartilhar e pesquisar de forma assíncrona experiências verificadas de depuração. | https://misakanet.org

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Python                                                                                 |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **527**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `action` · `agents` · `cloudflare-workers` · `codex` · `cordis-plugin` · `d1` · `deepseek-harness` · `deepseek-harness-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ikalus1988--misakanet/f6853900d49aba17.jpg" width="100%" alt="Ikalus1988/MisakaNet screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tingly-dev/tingly-box">tingly-dev/tingly-box</a></b> · ⭐353 · Go · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Your Intelligence, Orchestrated. Any Model, Any Agent, Any One.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Go                                                                                     |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **353**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `claude-code` · `dsh` · `dsh-plugin` · `gateway` · `golang` · `harness` · `llm` · `open-source`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/54666b3bdc5c6195.png" width="100%" alt="tingly-dev/tingly-box screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tingly-dev--tingly-box/0ef2aa2f5bc4239d.gif" width="100%" alt="tingly-dev/tingly-box animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/acryldev/acryl">acryldev/acryl</a></b> · ⭐257 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

ACRYL - Agent Context Relay Yielding Lifecycles. One persistent workspace, one canonical context, any coding agent.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **257**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `acryl` · `agent-context-relay` · `agentic` · `agentic-ai` · `agentic-coding` · `agentic-development-environment` · `agentic-workflow` · `agentic-workflows`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/acryldev--acryl/47cfe6b23e87eea1.png" width="100%" alt="acryldev/acryl screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/luobosibing2/dsh-jev-plugin">luobosibing2/dsh-jev-plugin</a></b> · ⭐207 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **207**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/wenbin-wb/dsh-bridge">wenbin-wb/dsh-bridge</a></b> · ⭐199 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

🚀 DeepSeek Harness 多通道远程访问与安全守护插件 | 局域网扫码直连、Cloudflare / 自建公网隧道、微信 / QQ / 飞书 / Telegram 机器人全生命周期对话 | 内置全协议访问安全认证、后台防篡改与容灾保命体系

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **199**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `cloudflare-tunnel` · `deepseek-harness` · `dsh` · `dsh-plugin` · `feishu` · `mobile` · `pwa` · `qq-bot`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wenbin-wb--dsh-bridge/d0ee292e99883caa.webp" width="100%" alt="wenbin-wb/dsh-bridge screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/xiajiajun516/dsh-config-manager">xiajiajun516/dsh-config-manager</a></b> · ⭐192 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **192**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `backup` · `cli` · `config-manager` · `configuration` · `cordis` · `deepseek` · `deepseek-harness` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/xiajiajun516--dsh-config-manager/95eb0411c14b8fcd.png" width="100%" alt="xiajiajun516/dsh-config-manager screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/WSL043/dsh-codex-subscription">WSL043/dsh-codex-subscription</a></b> · ⭐182 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **182**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-agent` · `chatgpt` · `chatgpt-plus` · `chatgpt-pro` · `chatgpt-subscription` · `codex` · `codex-cli-alternative` · `codex-subscription`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/wsl043--dsh-codex-subscription/2c813d2312e069f3.webp" width="100%" alt="WSL043/dsh-codex-subscription screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐172 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code 桌面主题

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
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Totoro-qaq/dsh-plugin-bridge">Totoro-qaq/dsh-plugin-bridge</a></b> · ⭐163 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **163**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-15 |

🏷 `context-migration` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `preset-migration` · `session-migration`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/568de849cd2e9608.png" width="100%" alt="Totoro-qaq/dsh-plugin-bridge screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/totoro-qaq--dsh-plugin-bridge/b4a12cab0ba15f06.gif" width="100%" alt="Totoro-qaq/dsh-plugin-bridge animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/yannicksong0106/dsh-550c-boot">yannicksong0106/dsh-550c-boot</a></b> · ⭐154 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

550C 开机动画 for DeepSeek Harness — 首帧由宿主半边注入，DSH 的 Loading 卡片不露脸；桌面原生标题栏按钮收编成终端配色 | 550C boot splash plugin for DSH

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **154**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `boot-splash` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `loading-animation` · `splash-screen` · `web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/yannicksong0106--dsh-550c-boot/8d4b5595a9704213.png" width="100%" alt="yannicksong0106/dsh-550c-boot screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/franksong2702/dsh-codex-connect">franksong2702/dsh-codex-connect</a></b> · ⭐150 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Use openai-codex models and image generation via ChatGPT OAuth for DeepSeek Harness.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **150**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `chatgpt` · `codex` · `deepseek-harness` · `dsh` · `dsh-plugin` · `gpt-image-2` · `oauth`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/franksong2702--dsh-codex-connect/4cbf6ea0bc489916.jpg" width="100%" alt="franksong2702/dsh-codex-connect screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/MichengAI/dsh-agency-agents">MichengAI/dsh-agency-agents</a></b> · ⭐131 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH Agency Agents — 为 DeepSeek Harness 提供 321 名可召唤的专业智能体 · 321 summonable domain experts for DeepSeek Harness

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **131**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-plugins`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/michengai--dsh-agency-agents/5ce2bd38a0654d89.webp" width="100%" alt="MichengAI/dsh-agency-agents screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐116 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Open-source GrokBot alternative built on DeepSeek Harness. Build your personal bot team: multiple personal agents with persistent memory, identities and permissions, extensible through DSH plugins.｜基于 DeepSeek Harness 的开源 GrokBot 平替：有长期记忆的个人 AI Bot 团队，支持多 Bot 协作、身份权限与插件生态扩展。MIT.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **116**    |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐93 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DeepSeek Harness (DSH) 插件：✨ 提示词一键增强 + 💬 语音识别（说完自动停·云端/本地双引擎）· 附 🔁 服务异常一键重启

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **93**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/leantoken">morluto/leantoken</a></b> · ⭐83 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Code intelligence for agents: find the code that matters and keep your context window and tokens lean.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Rust                                                                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **83**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `ai-coding` · `code-intelligence` · `code-navigation` · `code-retrieval` · `code-search` · `codebase-indexing` · `coding-agents` · `context-engineering`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--leantoken/38b3e8f4a7b20aea.jpg" width="100%" alt="morluto/leantoken screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/cloader/dsh-taskboard">cloader/dsh-taskboard</a></b> · ⭐66 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

deepseekharness 任务看板插件

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **66**     |
| Last push    | 2026-10-16 |
| First listed | 2026-10-16 |

🏷 `agent` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `kanban` · `task-board`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/cloader--dsh-taskboard/cfd9efd4514a0b8f.png" width="100%" alt="cloader/dsh-taskboard screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 71</sub></summary>

- [strukto-ai/mirage](https://github.com/strukto-ai/mirage) - The World.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Uma proteção pré-execução para agentes de programação com AI.
- [daha1216/dsh-adult-tension](https://github.com/daha1216/dsh-adult-tension) - DeepSeek 自带破甲 18+ 互动叙事：活人感 NPC（自主决策/拒绝迎合）、211个世界与上万素材、开局随心定制、世界自行运转、零漂移存档.
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins DSH / DSH Plugin Marketplace: navegue, instale e atualize…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑.
- [arcships/rutis](https://github.com/arcships/rutis) - Um runtime de plugins para softwares que iteram sobre si mesmos — a base onde…
- [wqty123/dsh-browser](https://github.com/wqty123/dsh-browser) - Shared real browser plugin for DeepSeek Harness.
- [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) - O diretório vivo de plugins do DeepSeek Harness — atualizado a cada hora…
- [PolinniZhong/dsh-knit](https://github.com/PolinniZhong/dsh-knit) - 面向 AI Coding Agent 的任务感知工作区上下文检索与生命周期追踪：按当前任务找到、组织并持续追踪最相关的文档、代码与媒体.
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Diretório selecionado de plugins do DeepSeek Harness (DSH) — mais de 280…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [songoao25/dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) - DeepSeek Harness (DSH) plugin: replaces the stats row under the composer with…
- [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) - DeepSeek Harness 的 Prompt 工具箱：别再复制粘贴——24 条深度模板随手点，/prompt 与智能推荐主动兜底，装好即用、可自定义.
- [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) - 【求⭐】🐋DSH Web UI…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agente de chat em grupo multiplataforma baseado no…
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…
- [omdsh-dev/dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) - Advisor - Pair a second model that passively reviews each turn and injects…
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) - 🐖 DeepSeek Harness 养成插件，也可作为 Windows/Linux/macOS 桌面宠物运行；支持成长、学习、打工、钓鱼、图鉴与换肤.
- [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) - OMK — Evidence-backed evaluation and observability for prompts, RAG, skills…
- [liustack/pptwise](https://github.com/liustack/pptwise) - A real PowerPoint, not HTML. Tell your AI what to cover and pptwise builds an…
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, ferramentas, habilidades e recursos de aprendizado do DeepSeek Harness…
- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) - An dsh plugin for role-based LLM retry&amp;fallback strategy. 基于角色的模型重试备用策略插件.
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [xyrrrrr-r/dsh-eval-control](https://github.com/xyrrrrr-r/dsh-eval-control) - Host-side DSH evaluation control plugin for aeval：一次评测试次的配置注入、预算封顶与证据归属.
- [S3K926/dsh-selfwake](https://github.com/S3K926/dsh-selfwake) - DSH（DeepSeek Harness）插件：到点主动开口…
- [czcdr/dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) - 第三方适配插件：把上游 REA（github.com/morluto/rea）的 MCP 服务接入 DeepSeek Harness，提供…
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [S3K926/dsh-memory-board](https://github.com/S3K926/dsh-memory-board) - DSH（DeepSeek Harness）插件：把一份基于文件的本地记忆档案（日记 / 状态 / 生长记录 / 事件流）搬进设置页面板…
- [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) - A bilingual, continuously maintained directory of plugins for DeepSeek Harness…
- [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) - DSH plugin: an IDE-grade Git tool window as a native dsh-better-sidebar tab…
- [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) - DSH Web UI 会话进度插件：输入框停靠区常驻进度条.
- [unStone/dsh-xray](https://github.com/unStone/dsh-xray) - Raio X dos plugins do DeepSeek Harness: capacidades declaradas versus…
- [walksls/dsh-degeneration-kit](https://github.com/walksls/dsh-degeneration-kit) - DSH 防退化套件：把退化的思考块从模型可见历史里折叠掉，到水位自动落档、压缩或换会话。两个插件，治崩不治失忆.
- [hxy91819/dsh-auth](https://github.com/hxy91819/dsh-auth) - Caddy-fronted administrator authentication for DeepSeek Harness: Argon2id…
- [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) - DSH Web UI 右侧小游戏面板：18 款离线小游戏.
- [yauntyour/DSH-Encrypt](https://github.com/yauntyour/DSH-Encrypt) - 跨版本兼容设计的 DeepSeek Harness…
- [dsh-plugin-lab/dsh-plugin-debugging](https://github.com/dsh-plugin-lab/dsh-plugin-debugging) - Your DSH agent can now inspect, diagnose, and fix its own runtime.
- [ItQianChen/dsh-github-flow](https://github.com/ItQianChen/dsh-github-flow) - 让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚!
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode no DeepSeek Harness — plugin DSH que mantém OpenCode Zen + modelos de…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Veja claramente cada ação observável dos agentes de codificação de IA.
- [chenkai2/dsh-daemon](https://github.com/chenkai2/dsh-daemon) - dsh daemon: register the DeepSeek Harness web server (dsh web) as an…
- [dsh-cc/dsh-cc](https://github.com/dsh-cc/dsh-cc) - A batteries-included coding agent for DeepSeek Harness — Claude Code-style…
- [henlii/dsh-plugins](https://github.com/henlii/dsh-plugins) - DSH plugin collection: password auth + trust for dsh web LAN/Tailscale access…
- [ltxlong/dsh-session-kit](https://github.com/ltxlong/dsh-session-kit) - 会话管理菜单、归档管理、轮次级删除、重新生成、记忆管理、任务管理、话题导航.
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) - Padrão de verificação sem dependências para plugins do DeepSeek Harness (dsh)…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web do DeepSeek Harness (DSH): aba lateral market-dashboard para…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [27painter/dsh-moli](https://github.com/27painter/dsh-moli) - DSH plugin · Drive the local Moli headless browser from DeepSeek Harness…
- [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) - DSH STORE — marketplace de plugins de terceiros e gerenciador protegido do…
- [Atelyx/Atelyx](https://github.com/Atelyx/Atelyx) - Atelyx é uma bancada de trabalho desktop extensível e centrada nas pessoas…
- [DoveLi-Gu/dsh-showcase](https://github.com/DoveLi-Gu/dsh-showcase) - Local, verifiable delivery evidence reports and DSH plugin for coding-agent…
- [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) - DSH Web 输入体验插件：发送/换行键位切换、右键菜单、面板滚动与尺寸记忆、OpenCode 请求头自动注入.
- [gluztm/DSHGuard](https://github.com/gluztm/DSHGuard) - DSH 守护壳：DeepSeek Harness 的一键启动与救援工具——改动前自动存档、出事整组回滚、本地管理插件、诊断日志导出；Web…
- [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) - DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动.
- [Mzy123l/dsh-plugin-remote-access](https://github.com/Mzy123l/dsh-plugin-remote-access) - 为 DeepSeek Harness 桌面版提供「限网段 + 可选数字密码」的远程访问入口.
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色：换装、白饭、摸头、问候、登录账户余额和本机今日用量预估.
- [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) - DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持…
- [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) - DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin do DeepSeek Harness: transforma a falha de provisionamento da ACL da…
- [akkefa/deepseek-cordis](https://github.com/akkefa/deepseek-cordis) - Python plugin runtime targeting DeepSeek Harness vendored Cordis semantics.
- [YYZ-YingSe/cordis-x](https://github.com/YYZ-YingSe/cordis-x) - An embeddable Rust plugin runtime with dependency-aware lifecycles and Rust…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [helloHupc/dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) - DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 |…
- [tellmewhattodo/dsh-serenity-plugin](https://github.com/tellmewhattodo/dsh-serenity-plugin) - dsh-serenity-plugin.

</details>

<a id="writing"></a>

## Textos, discussões e vídeos

Textos, discussões e vídeos sobre a capacidade de mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐16 · 👁️ observed · 1 天</summary>

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
| First listed | 2026-10-15 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 8 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 14 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 6 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| First listed | 2026-10-16 |

</details>

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 14 天</summary>

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
| TypeScript | 390      | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 80       | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 38       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 26       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 15       | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 9        | `persiyanov/herdr-reviewr`, `afarrell/claude-meter`, `hey-yvan/claude-quota-bar`                              |
| Go         | 6        | `vulcanshen/ccdrawu`, `Gaurav-Gosain/tuios`, `3xDevOps/aether`                                                |
| C          | 1        | `reporails/arcade`                                                                                            |
| C#         | 1        | `gluztm/DSHGuard`                                                                                             |
| PowerShell | 1        | `Nader-mech/claude-statusline`                                                                                |
| Ruby       | 1        | `romacv/claude-plan-usage-statusline`                                                                         |
| Swift      | 1        | `michalstrnadel/AgentBar`                                                                                     |
| jq         | 1        | `n0nuser/claude-statusline`                                                                                   |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Correções são bem-vindas e são a maneira mais rápida de melhorar esta lista. Abra uma issue ou um pull request se uma entrada estiver na categoria errada, com a classificação errada ou se um projeto tiver sido excluído indevidamente por colisão de nome — essa é a categoria em que filtros automatizados têm maior probabilidade de errar.

---

<sub>Projeto independente da comunidade. Não afiliado, endossado nem revisado por Anthropic. Claude Code, Claude e Anthropic são marcas registradas de Anthropic. O comportamento do produto pode mudar sem aviso; verifique tudo o que for essencial na documentação oficial. Os ativos permanecem propriedade de seus projetos de origem e são reproduzidos somente quando uma licença permite.</sub>

<sub>Last updated · 2026-10-16T23:45:14+08:00</sub>
