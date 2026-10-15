<p align="center">
  <img src="../assets/readme/hero.png" width="100%" alt="Mods incríveis do Claude">
</p>

<h1 align="center">Mods incríveis do Claude</h1>

<p align="center"><b>O índice de mods e plugins do Claude Code classificados por evidências, além dos comportamentos mais profundos que eles alteram.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-610-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
  <a href="https://wh000wh000.github.io/awesome-claude-mods/"><img src="https://img.shields.io/badge/site-searchable-1f6feb" alt="site"></a>
</p>

<p align="center"><sub><a href="../README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Português</b> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Índice ativo** · Última sincronização: `2026-10-15T23:16:19+08:00` (UTC+8)
> · Entradas: **610** · Adicionadas na atualização mais recente: **0** · Linguagens de implementação: **11**

<sub>Cada entrada abaixo foi coletada, filtrada e verificada novamente de forma automática. Nada aqui é uma inserção paga.</sub>

<a id="featured"></a>

## Destaques do momento

<sub>Uma entrada por categoria, classificada pelo grau de evidência e pelo número de estrelas, recalculada a cada atualização. É uma classificação, não uma recomendação; cada destaque leva ao respectivo card completo abaixo. Projetos que publicaram uma captura de tela ou uma gravação têm preferência, para que a faixa continue visual.</sub>

<table>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action">
<b>🏛️ <a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b>
<sub>⭐9523 · TypeScript · ✅ official</sub>
</td>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/alexgreensh/token-optimizer/main/skills/token-optimizer/assets/dashboard-demo.gif" width="100%" alt="alexgreensh/token-optimizer">
<b>🧩 <a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b>
<sub>⭐2566 · Python · 👁️ observed</sub>
<sub>Encontre os tokens fantasmas. Corrija-os. Sobreviva à compactação. Evite a degradação da qualidade do contexto.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo">
<b>🧵 <a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b>
<sub>⭐74863 · TypeScript · 👁️ observed</sub>
<sub>🌊 O agent harness original. Implante enxames inteligentes multiagente, coordene fluxos de trabalho autônomos e crie sistemas de IA conversacional. Inclui memória…</sub>
</td>
<td width="50%" valign="top">
<b>📰 <a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b>
<sub>⭐15 · 👁️ observed</sub>
</td>
</tr>
</table>

## Conteúdo

- [O que é um mod do Claude Code](#o-que-é-um-mod-do-claude-code)
- [Como as entradas são classificadas](#como-as-entradas-são-classificadas)
- [Oficial: repositórios próprios de Anthropic e notas de versão](#oficial-repositórios-próprios-de-anthropic-e-notas-de-versão) — **16**
- [Mods: criados com a capacidade de modificação](#mods-criados-com-a-capacidade-de-modificação) — **474**
- [Ecossistemas de plugins do DSH e do Cordis](#ecossistemas-de-plugins-do-dsh-e-do-cordis) — **112**
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
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code">anthropics/claude-code</a></b> · ⭐151011 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **151011** |
| Last push    | 2026-10-14 |
| First listed | 2026-10-04 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-action">anthropics/claude-code-action</a></b> · ⭐9523 · TypeScript · ✅ official · 0 天</summary>

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
| Stars        | **9523**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anthropics--claude-code-action/b852b554eaf6a231.jpg" width="100%" alt="anthropics/claude-code-action screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-python">anthropics/claude-agent-sdk-python</a></b> · ⭐8285 · Python · ✅ official · 0 天</summary>

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
| Stars        | **8285**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-code-security-review">anthropics/claude-code-security-review</a></b> · ⭐6390 · Python · ✅ official · 245 天</summary>

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
| Stars        | **6390**   |
| Last push    | 2026-02-11 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/claude-agent-sdk-typescript">anthropics/claude-agent-sdk-typescript</a></b> · ⭐1812 · Shell · ✅ official · 0 天</summary>

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
| Stars        | **1812**   |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

</details>

<details>
<summary>🏛️ <b><a href="https://github.com/anthropics/model-cards">anthropics/model-cards</a></b> · ⭐25 · ✅ official · 313 天</summary>

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
<summary><b>Mais nesta categoria</b> <sub>· 4</sub></summary>

- [Claude Code 2.1.295 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Adicionado `$.ui.notify` aos mods: emite uma notificação nativa usando sua…
- [Claude Code 2.1.296 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Corrigido o Esc ou uma interrupção durante um hook de `UserPromptSubmit` ou o…
- [Claude Code 2.1.299 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `$.prompt.media` so a `prompt.submit` hook of a mod installed by managed…
- [Claude Code 2.1.300 — the mod surface](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) - Added `virtualText` to a mod.

</details>

<a id="mods"></a>

## Mods: criados com a capacidade de modificação

Cada entrada aqui apresenta evidências do uso da capacidade que o Claude Code adquiriu na versão 2.1.287: ela desenha por meio de `ui.render`, possui um painel, faixa ou cartão, lê `$.ui.selection()`, cria companheiros de equipe com `agent.spawn` ou afirma claramente que é um mod.

<details>
<summary>🧩 <b><a href="https://github.com/alexgreensh/token-optimizer">alexgreensh/token-optimizer</a></b> · ⭐2566 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **2566**   |
| Last push    | 2026-10-15 |
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
<summary>🧩 <b><a href="https://github.com/YeonwooSung/my-claude-code-mods">YeonwooSung/my-claude-code-mods</a></b> · ⭐820 · TypeScript · 👁️ observed · 1 天</summary>

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
| Stars        | **820**    |
| Last push    | 2026-10-14 |
| First listed | 2026-10-15 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/awesome-claude-code-mods">karanb192/awesome-claude-code-mods</a></b> · ⭐586 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **586**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `anthropic` · `awesome` · `awesome-list` · `claude` · `claude-code` · `claude-code-hooks` · `claude-code-mods` · `claude-code-plugin`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/hamzafer/claude-code-mods">hamzafer/claude-code-mods</a></b> · ⭐251 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **251**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugins` · `developer-tools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/c683a5d95e78d920.png" width="100%" alt="hamzafer/claude-code-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hamzafer--claude-code-mods/0b4dc7c7692bd024.gif" width="100%" alt="hamzafer/claude-code-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/iamumeransari/claude-show-your-work">iamumeransari/claude-show-your-work</a></b> · ⭐209 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **209**    |
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
<summary>🧩 <b><a href="https://github.com/HeyCubit/effortless">HeyCubit/effortless</a></b> · ⭐204 · HTML · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: picks the reasoning effort for every prompt, shows the prompt cache and context, and hands off or compacts in one click

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
| Stars        | **204**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-tools` · `anthropic` · `claude` · `claude-code` · `claude-code-plugin` · `developer-tools` · `prompt-caching`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/ad0a6472f7a34cd7.png" width="100%" alt="HeyCubit/effortless screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/heycubit--effortless/fcef2f9593961020.gif" width="100%" alt="HeyCubit/effortless animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/karanb192/cache-tax">karanb192/cache-tax</a></b> · ⭐192 · TypeScript · 👁️ observed · 11 天</summary>

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
| Stars        | **192**    |
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
<summary>🧩 <b><a href="https://github.com/hellosverre/claude-skins">hellosverre/claude-skins</a></b> · ⭐149 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **149**    |
| Last push    | 2026-10-14 |
| First listed | 2026-10-13 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-mods` · `claude-code-plugin` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/hellosverre--claude-skins/e70c992c52ca2e70.gif" width="100%" alt="hellosverre/claude-skins animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/NahumLitvin/prismantis">NahumLitvin/prismantis</a></b> · ⭐112 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **112**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `markdown` · `mermaid` · `terminal` · `theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/f6e44059e77434b4.png" width="100%" alt="NahumLitvin/prismantis screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nahumlitvin--prismantis/00e2cffa219a3511.gif" width="100%" alt="NahumLitvin/prismantis animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/cablate/ctx-handoff-mod">cablate/ctx-handoff-mod</a></b> · ⭐97 · TypeScript · 👁️ observed · 0 天</summary>

##### 📝 Summary

Claude Code mod: hands off to a fresh conversation when context fills up, keeps the cache warm while you're away, and turns what you teach Claude into project notes

<sub>🔧 Encontrado em uso no código: `docs/guide.md`, `docs/guide.zh-TW.md`</sub>

##### 📌 Basic facts

| Field     | Value                                                                 |
| --------- | --------------------------------------------------------------------- |
| Category  | `Mods: criados com a capacidade de modificação`                       |
| Evidence  | `o próprio texto menciona um mod API ou declara a capacidade de mods` |
| Linguagem | TypeScript                                                            |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **97**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-coding` · `anthropic` · `claude` · `claude-code` · `claude-code-mod` · `claude-code-plugin` · `context-management` · `prompt-caching`

</details>

<details>
<summary>🧩 <b><a href="https://github.com/scasella/claude-flightdeck">scasella/claude-flightdeck</a></b> · ⭐90 · TypeScript · 👁️ observed · 3 天</summary>

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
| Stars        | **90**     |
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
<summary>🧩 <b><a href="https://github.com/Tickloop/claude-mods">Tickloop/claude-mods</a></b> · ⭐80 · TypeScript · 👁️ observed · 6 天</summary>

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
<summary>🧩 <b><a href="https://github.com/zycck/claude-mods">zycck/claude-mods</a></b> · ⭐53 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **53**     |
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/49f09d1600b02c7a.gif" width="100%" alt="zycck/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zycck--claude-mods/25f4230871cb30f6.gif" width="100%" alt="zycck/claude-mods animation"><br><sub>gravação animada · <a href="https://raw.githubusercontent.com/zycck/claude-mods/main/media/plan-progress.mp4">Abrir vídeo</a></sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/oikon48/prompt-rail">oikon48/prompt-rail</a></b> · ⭐32 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **32**     |
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
<summary>🧩 <b><a href="https://github.com/tzafrir/human-in-the-loop">tzafrir/human-in-the-loop</a></b> · ⭐29 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **29**     |
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
<summary>🧩 <b><a href="https://github.com/dgokcin/claude-pokemon-mod">dgokcin/claude-pokemon-mod</a></b> · ⭐27 · JavaScript · 👁️ observed · 0 天</summary>

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
| Stars        | **27**     |
| Last push    | 2026-10-14 |
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
<summary>🧩 <b><a href="https://github.com/Jhonatan-de-Souza/ClaudeMods">Jhonatan-de-Souza/ClaudeMods</a></b> · ⭐24 · TypeScript · 👁️ observed · 1 天</summary>

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
<summary>🧩 <b><a href="https://github.com/lemomo-ai/lemo-mod">lemomo-ai/lemo-mod</a></b> · ⭐22 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-starter-kit">promptadvisers/claude-mods-starter-kit</a></b> · ⭐20 · JavaScript · 👁️ observed · 12 天</summary>

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
<summary>🧩 <b><a href="https://github.com/promptadvisers/claude-mods-computer-use-threads">promptadvisers/claude-mods-computer-use-threads</a></b> · ⭐16 · JavaScript · 👁️ observed · 9 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Unayung/cc-mods-enil">Unayung/cc-mods-enil</a></b> · ⭐15 · TypeScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/JetsonChan/CC-Usage-Band">JetsonChan/CC-Usage-Band</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
<summary>🧩 <b><a href="https://github.com/OneWave-AI/claude-code-mods">OneWave-AI/claude-code-mods</a></b> · ⭐14 · TypeScript · 👁️ observed · 12 天</summary>

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
| Stars        | **14**     |
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
<summary>🧩 <b><a href="https://github.com/aieo-product/claude_qamods">aieo-product/claude_qamods</a></b> · ⭐12 · TypeScript · 👁️ observed · 8 天</summary>

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
<summary>🧩 <b><a href="https://github.com/augiefra/claude-mods">augiefra/claude-mods</a></b> · ⭐12 · JavaScript · 👁️ observed · 2 天</summary>

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
<summary>🧩 <b><a href="https://github.com/ersinkoc/claude-mods">ersinkoc/claude-mods</a></b> · ⭐11 · TypeScript · 👁️ observed · 5 天</summary>

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
| Stars        | **11**     |
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
<summary>🧩 <b><a href="https://github.com/furqan-khan07/pixelband">furqan-khan07/pixelband</a></b> · ⭐10 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/VedantAndhale/claude-pro-kit">VedantAndhale/claude-pro-kit</a></b> · ⭐10 · TypeScript · 👁️ observed · 5 天</summary>

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
<summary>🧩 <b><a href="https://github.com/Arunjay4213/claude-mods">Arunjay4213/claude-mods</a></b> · ⭐9 · TypeScript · 👁️ observed · 29 天</summary>

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
<summary>🧩 <b><a href="https://github.com/deepsteve/deepsteve">deepsteve/deepsteve</a></b> · ⭐9 · JavaScript · 👁️ observed · 1 天</summary>

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
| Last push    | 2026-10-14 |
| First listed | 2026-10-11 |

🏷 `ai-coding` · `ai-tools` · `browser-terminal` · `claude-code` · `codex` · `coding-agent` · `developer-tools` · `devtools`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/deepsteve--deepsteve/adee5ea71e2e3289.png" width="100%" alt="deepsteve/deepsteve screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/az9713/claude-mod-pack">az9713/claude-mod-pack</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
<summary>🧩 <b><a href="https://github.com/devbrother2024/devbrothers-mods">devbrother2024/devbrothers-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 11 天</summary>

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
| Stars        | **8**      |
| Last push    | 2026-10-04 |
| First listed | 2026-10-11 |

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="devbrother2024/devbrothers-mods screenshot"></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/devbrother2024--devbrothers-mods/10df726087fd2881.webp" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@%EA%B0%9C%EB%B0%9C%EB%8F%99%EC%83%9D">Assistir em youtube.com</a> · a reprodução é aberta no site de origem; GitHub não pode incorporá-la em linha</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/mishgoldenberg/claude-mods">mishgoldenberg/claude-mods</a></b> · ⭐8 · TypeScript · 👁️ observed · 8 天</summary>

##### 📝 Summary

Painéis, proteções e mods de qualidade de vida para Claude Code: contexto, uso, atividade ao vivo, notificações, regras de segurança, orientador de prompts e central de comandos.

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
| Last push    | 2026-10-06 |
| First listed | 2026-10-11 |

🏷 `ai-agents` · `ai-safety` · `anthropic` · `claude` · `claude-code` · `claude-code-plugins` · `developer-tools` · `llm`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/mishgoldenberg--claude-mods/9458e91720f67521.gif" width="100%" alt="mishgoldenberg/claude-mods animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧩 <b><a href="https://github.com/Danovich/turntype">Danovich/turntype</a></b> · ⭐7 · TypeScript · 👁️ observed · 3 天</summary>

##### 📝 Summary

Um teste de digitação para passar o tempo enquanto Claude trabalha. Um mod de código do Claude.

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
| Last push    | 2026-10-11 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `claude-code-mod` · `claude-code-plugin` · `claude-mods` · `typing` · `typing-game` · `typing-practice` · `typing-test`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/danovich--turntype/24d5c7d94e15fcfb.gif" width="100%" alt="Danovich/turntype animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 440</sub></summary>

- [whyashthakker/awesome-claude-code-mods](https://github.com/whyashthakker/awesome-claude-code-mods) - Coleção de mais de 100 mods que você pode usar com Claude Code.
- [darrell-tw/darrelltw-mods](https://github.com/darrell-tw/darrelltw-mods) - Mods do Claude Code criados por Darrell Wang — faixas acima do prompt, sem…
- [ray-amjad/claude-code-mods](https://github.com/ray-amjad/claude-code-mods) - Mods de Claude Code de Ray Amjad: painéis, faixas, proteções de prompt…
- [0xDarkMatter/claude-mods](https://github.com/0xDarkMatter/claude-mods) - Skills, agentes, comandos, regras, hooks e estilos de saída especializados para…
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods) - Mods do Claude e as ferramentas para criá-los: primeiro uma skill de criação…
- [nateherkai/claude-code-mods](https://github.com/nateherkai/claude-code-mods) - Quatro mods do Claude Code: Cache Keeper, Recording Mode, Goal Meter e…
- [ucsandman/claude-harness](https://github.com/ucsandman/claude-harness) - O harness do Claude Code que uso todos os dias, publicado com este nome desde o…
- [kagamiurayama/claude-code-roof-mod](https://github.com/kagamiurayama/claude-code-roof-mod) - Troque o telhado do Claude Code usando Claude Mods: sem alterar o binário…
- [RiskAverseTech/toolgate](https://github.com/RiskAverseTech/toolgate) - A measured tool-call firewall for AI agents: allow, ask or deny before the…
- [artemnovichkov/xcode-mods](https://github.com/artemnovichkov/xcode-mods) - Build, testes, console e prévias do SwiftUI do Xcode dentro do Claude Code.
- [BrianHuang813/clawd-actor](https://github.com/BrianHuang813/clawd-actor) - Mod do Claude Code: Clawd encena o que Claude está fazendo, acima do prompt.
- [nvr0x5/claude-deck](https://github.com/nvr0x5/claude-deck) - A cockpit for Claude Code: live plan bars, subagent strips, usage limits with…
- [centminmod/claude-plugins](https://github.com/centminmod/claude-plugins) - Personal Claude Code plugin marketplace — session-metrics, more to come.
- [AgriciDaniel/claude-mods-brain](https://github.com/AgriciDaniel/claude-mods-brain) - Base de conhecimento do Obsidian com fontes citadas sobre Claude Code mods…
- [Hangghost/learning-hacker-claude-mod](https://github.com/Hangghost/learning-hacker-claude-mod) - Mods do Claude Code do Learning Hacker: transforme o funcionamento do agent em…
- [kakha13/claude](https://github.com/kakha13/claude) - Mods do Claude Code que corrigem e traduzem seus prompts antes que Claude os…
- [nekyialabs/claude-code-toolkit](https://github.com/nekyialabs/claude-code-toolkit) - Mods e skills de Claude Code do Nekyia Labs, criados e usados diariamente por…
- [letswritetw/claude-mod-open-todos](https://github.com/letswritetw/claude-mod-open-todos) - Painel lateral do Claude Desktop (aba Code): lista todos os afazeres inacabados…
- [letswritetw/claude-mod-token-usage](https://github.com/letswritetw/claude-mod-token-usage) - Barra de uso acima da caixa de entrada do Claude Desktop (aba Code): cota de 5h…
- [xuanji86/claude-agentpane](https://github.com/xuanji86/claude-agentpane) - Um painel lateral para o código Claude: os subagentes executados por uma…
- [KilimcininKorOglu/claude-code-mods](https://github.com/KilimcininKorOglu/claude-code-mods) - Mods de Claude (plugins de hooks de função) para Claude Code.
- [BeLazy167/claude-mods-skill](https://github.com/BeLazy167/claude-mods-skill) - Skill que ensina agentes do Claude Code a criar Claude Mods.
- [omarcevi/claudemods](https://github.com/omarcevi/claudemods) - Mods, plugins e skills comunitários do Claude, instaláveis em um único mercado.
- [xuanji86/claude-statuspane](https://github.com/xuanji86/claude-statuspane) - Um cartão de status flutuante para o Claude Code — modelo, contexto, limites de…
- [bruw/workflow-conductor](https://github.com/bruw/workflow-conductor) - Visual workflow planner in Claude Code.
- [davekiss/mods](https://github.com/davekiss/mods) - Mods do Claude Code por Dave Kiss.
- [baselane-sh/mods-catalog](https://github.com/baselane-sh/mods-catalog) - A galeria de mods do Baselane: mods de Claude Code, verificados e fixados.
- [eighteyes/cactus](https://github.com/eighteyes/cactus) - Uma fila de decisões CLI/TUI para humanos que trabalham com agentes…
- [ice-lfernandes/claude-code-mods](https://github.com/ice-lfernandes/claude-code-mods) - Seis mods de Claude Code: limites do plano e contexto acima do prompt, um…
- [natsukium/claude-code-figures-plugin](https://github.com/natsukium/claude-code-figures-plugin) - Draw diagrams, LaTeX math, and tool-result images inline in kitty-graphics…
- [neteye-platform/cc-split-diff-view](https://github.com/neteye-platform/cc-split-diff-view) - Mod do Claude Code que desenha diffs de Edit e Write em duas colunas lado a lado.
- [ronanworks/claude-code-mods](https://github.com/ronanworks/claude-code-mods) - Mods de Claude Code: painel de uso 像素螃蟹 usage-hud + links HTML clicáveis no…
- [timoncool/givememod](https://github.com/timoncool/givememod) - Mods de código do Claude sob demanda — uma habilidade que lê sua conversa e…
- [arasovic/claude-code-mods](https://github.com/arasovic/claude-code-mods) - Mods para o Claude Code: plugins de function-hook que adicionam painéis…
- [danyuchn/claude-mods](https://github.com/danyuchn/claude-mods) - Mods de Claude Code: screen-guard oculta nomes e segredos enquanto você…
- [GarvitNangru/claude-code-mods](https://github.com/GarvitNangru/claude-code-mods) - Mods e skins para Claude Code: uma barra de progresso ao vivo para as tarefas…
- [helenkwok/gsd-status-mod](https://github.com/helenkwok/gsd-status-mod) - Live GSD dashboard for Claude Code: roadmap, agent tree with forks, context and…
- [hellosverre/mod-store](https://github.com/hellosverre/mod-store) - Uma loja de aplicativos para mods do Claude Code, dentro do Claude Code: /mods…
- [magidandrew/cx](https://github.com/magidandrew/cx) - Extensões do Claude Code. Desbloqueie todo o poder do Claude.
- [markneonin/paneline](https://github.com/markneonin/paneline) - Mod (plugin) do Claude Code que adiciona um painel lateral com abas Activity…
- [ofeklevy11/claude-code-hud](https://github.com/ofeklevy11/claude-code-hud) - Dois mods de Claude Code acima da caixa de prompt: medidor da janela de…
- [Szotasz/claude-mods](https://github.com/Szotasz/claude-mods) - Marketplace dos meus mods do Claude Code.
- [xuanji86/claude-mdview](https://github.com/xuanji86/claude-mdview) - Leia os arquivos Markdown nomeados pelo código Claude, renderizados ao lado da…
- [Antreas-Strb/glanceflow](https://github.com/Antreas-Strb/glanceflow) - GlanceFlow para Claude Code: uma checklist calma acima do prompt mostrando o…
- [Boom-Vitt/boombignose-mods](https://github.com/Boom-Vitt/boombignose-mods) - Mods de Claude Code: barra de contexto, painel de agentes, desfoque PDPA.
- [hahmjuntae/claude-mods-image-preview](https://github.com/hahmjuntae/claude-mods-image-preview) - Mod de Claude Code: miniaturas de imagens coladas acima do prompt, em qualquer…
- [leopiney/wolfbud-claude-mod](https://github.com/leopiney/wolfbud-claude-mod) - Colega de trabalho por voz para o Claude Code.
- [Nongfsq/frank-claude-cockpit](https://github.com/Nongfsq/frank-claude-cockpit) - Dois mods de Claude Code para executar muitas sessões simultaneamente: um…
- [borabiricik/claude-mods](https://github.com/borabiricik/claude-mods) - Mods de Claude Code: typing-speed, um velocímetro de digitação ao vivo com…
- [dougcunha/claude-mods](https://github.com/dougcunha/claude-mods) - Mods para o Claude Code: painéis, comandos e hooks criados com o plugin…
- [DrishtantKaushal/AwesomeClaudeCodeMods](https://github.com/DrishtantKaushal/AwesomeClaudeCodeMods) - Descubra mods, plugins e extensões de Claude Code com demonstrações animadas…
- [galElmalah/claude-mods](https://github.com/galElmalah/claude-mods) - Mod de Claude Code: diagramas mermaid desenhados diretamente na transcrição.
- [ha-ptt0601/cc-mods](https://github.com/ha-ptt0601/cc-mods) - Pequenos mods do Claude Code (plugins de function-hook): session-switcher e mais.
- [LeeHigma0201/claude-code-mods](https://github.com/LeeHigma0201/claude-code-mods) - Mods de Claude Code: mod-scout (encontre os mods que você mais usaria)…
- [mertkayacs/ultramod](https://github.com/mertkayacs/ultramod) - the best all-in-one mod pack for Claude Code.
- [NarenDawar/narens-claude-toolkit](https://github.com/NarenDawar/narens-claude-toolkit) - Kit de ferramentas de Naren para Claude: skills, mods e servidores MCP para o…
- [nuromirzak/nibbl](https://github.com/nuromirzak/nibbl) - A tiny pixel pet that nibbles your bugs. Lives above your Claude Code prompt.
- [theonly1me/claude-code-mods](https://github.com/theonly1me/claude-code-mods) - Vários mods do claude code criados por mim.
- [ayagmar/claude-modmgr](https://github.com/ayagmar/claude-modmgr) - modmgr: descubra, inspecione, alterne e atualize mods de Claude Code.
- [claude-code-mods/best-claude-code-mods](https://github.com/claude-code-mods/best-claude-code-mods) - Melhores mods de Claude Code: selecionados, validados e fixados.
- [comertial/claude-pending-changes](https://github.com/comertial/claude-pending-changes) - Review every file Claude touches, like a pull request, without leaving the…
- [comertial/comertial-mods](https://github.com/comertial/comertial-mods) - Mods do Claude Code para Engineers de verdade.
- [dominicrico/jev-router](https://github.com/dominicrico/jev-router) - Plugin do Claude Code: roteamento automático de modelos Claude.
- [FynnXland/fynn-mods](https://github.com/FynnXland/fynn-mods) - Seis mods para Claude Code: mascote Clawd animado, barras de limite de uso e…
- [Hula-Hoop-AI/supermods](https://github.com/Hula-Hoop-AI/supermods) - Um marketplace de mods para Claude Code: depurador passo a passo para o loop do…
- [ibrahimkobeissy/claude-mods](https://github.com/ibrahimkobeissy/claude-mods) - Mods de código de código aberto para o Claude Code: painéis, linhas de status…
- [Malkiz/claude-reply-comments](https://github.com/Malkiz/claude-reply-comments) - Mod de Claude Code: responda a Claude ponto por ponto, diretamente no texto.
- [nextscape/ns-mods](https://github.com/nextscape/ns-mods) - Nextscape が公開する Claude Code mod（関数フックのプラグイン）集。使う mod を選んで導入できるマーケットプレイス.
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
- [xsyetopz/claudetto](https://github.com/xsyetopz/claudetto) - A very opinionated Claude Code plugin designed by a Rustacean obsessed with…
- [yash-gadodia/claude-mods](https://github.com/yash-gadodia/claude-mods) - Mods de Claude Code que mantêm um agente honesto — hooks de função que protegem…
- [agentic-workbench/agent-quick-menu](https://github.com/agentic-workbench/agent-quick-menu) - Quick menu for Claude Code: every plugin.
- [alexcz-a11y/claude-mods](https://github.com/alexcz-a11y/claude-mods) - My collection of Claude Code mods, one mod per directory.
- [AlexeyHRDesign/colorwheel](https://github.com/AlexeyHRDesign/colorwheel) - Themed replies, full-width diagrams, and your context and limits at a glance…
- [gaius-codius/ostrakon](https://github.com/gaius-codius/ostrakon) - Um mod de Claude Code para capturar pensamentos durante o trabalho…
- [helenlin0621/tea-egg](https://github.com/helenlin0621/tea-egg) - Cultive um ovo de chá que ganha sabor lentamente enquanto você escreve código ·…
- [herman925/925-cc-plugins](https://github.com/herman925/925-cc-plugins) - Mods do Claude Code de Herman (marketplace herman-mods).
- [Krs7N/context-meter](https://github.com/Krs7N/context-meter) - Live context-window meter above the Claude Code prompt: animated fill bar…
- [lorenzh/rabe](https://github.com/lorenzh/rabe) - Veja o que o Claude Code executa em segundo plano: subagentes, tarefas de…
- [MankhongGarden/claude-code-mods-field-notes](https://github.com/MankhongGarden/claude-code-mods-field-notes) - Notas de campo do primeiro dia sobre mods do Claude Code no Windows: uma barra…
- [midudev/better-claude](https://github.com/midudev/better-claude) - Small plugins and mods that make your life (and Claude Code) better.
- [patitow/claude-mod-cost-visibility](https://github.com/patitow/claude-mod-cost-visibility) - Mod do Claude Code: medidores ao vivo de custo, contexto e cota do plano acima…
- [revenantworks/claude-skills](https://github.com/revenantworks/claude-skills) - 28 Agent Skills for Claude in five packs.
- [ruslanshchuchkin/claude-techno-mod](https://github.com/ruslanshchuchkin/claude-techno-mod) - 😈 We are making some TECHNO babyyyy 😈.
- [Ryan-LT/claude-mods](https://github.com/Ryan-LT/claude-mods) - Claude Code mods: always-on usage-limits band.
- [Sennjen/claude-sdlc](https://github.com/Sennjen/claude-sdlc) - Plugin e mod do Claude Code: um SDLC nativo de IA.
- [tiger42/claude-mods](https://github.com/tiger42/claude-mods) - My personal Claude mods.
- [timoncool/slapbox](https://github.com/timoncool/slapbox) - 🍑 Dê uma palmada em Claude quando ele fizer besteira — um mod de alívio de…
- [UtsavBalar1231/oh-my-claudeagent](https://github.com/UtsavBalar1231/oh-my-claudeagent) - Claude Code, com comprovantes. Um plugin que planeja, delega e comprova que o…
- [vulcanshen/ccdrawu](https://github.com/vulcanshen/ccdrawu) - A sidebar for Claude Code: usage limits, context, model, cost, git and session…
- [yodakeisuke/claudelingo](https://github.com/yodakeisuke/claudelingo) - Aprenda um idioma estrangeiro enquanto trabalha com o código Claude.
- [AmiTu1020/mods-context-auto-handoff-public](https://github.com/AmiTu1020/mods-context-auto-handoff-public) - Claude Code mod：context 快滿時自動寫交接卡、開新對話接手（可設定項目與檢查，交接中鎖工具）.
- [andrewbakercloudscale/claude-code-cost-sidebar](https://github.com/andrewbakercloudscale/claude-code-cost-sidebar) - Barra lateral de custos, tokens e uso de contexto em tempo real para Claude…
- [Azertyuiop442/deepshrink](https://github.com/Azertyuiop442/deepshrink) - Proven-freshness context store for coding agents - mtime-verified reuse, TF-IDF…
- [bradtraversy/claude-mods](https://github.com/bradtraversy/claude-mods) - Personal Claude Code mods for interface customization, safety, and verification.
- [cga-management/claude-decisions](https://github.com/cga-management/claude-decisions) - Claude Code mod: a Decisions pane that tracks the open decisions Claude raises…
- [cldotdev/claude-todo-list](https://github.com/cldotdev/claude-todo-list) - Um mod do Claude Code que mantém uma lista atualizada dos itens em aberto em…
- [connectwithub/loopkeeper](https://github.com/connectwithub/loopkeeper) - Mantenha o Claude Code dentro de um plano: etapas, portões de aprovação e um…
- [Davron2004/slash-coverage](https://github.com/Davron2004/slash-coverage) - Veja quais arquivos cada agente do Claude Code tem em seu contexto, e quanto de…
- [daydeda/daymods](https://github.com/daydeda/daymods) - Small, independent mods for Claude Code: install only the ones you want.
- [enhki/claude-mods](https://github.com/enhki/claude-mods) - Pequenos mods do Claude Code para o terminal e o aplicativo desktop.
- [Exdenta/ambient-spanish](https://github.com/Exdenta/ambient-spanish) - Habilidade + mod Claude CLI que adiciona palavras em espanhol às respostas do…
- [FrBmt-BIGetNouf/alarum-claude-mod](https://github.com/FrBmt-BIGetNouf/alarum-claude-mod) - Seus eventos do Alarum acima do prompt do Claude Code: o que acabou de chegar e…
- [FrBmt-BIGetNouf/floatee-claude-mod](https://github.com/FrBmt-BIGetNouf/floatee-claude-mod) - Seu backlog Floatee acima do prompt do Claude Code: execute, guie e marque seus…
- [HenriqueRicieri/session-hud](https://github.com/HenriqueRicieri/session-hud) - Claude Code mod: context, plan limits and session cost in a one-line band above…
- [HyunjunJeon/claude-workflow-mods](https://github.com/HyunjunJeon/claude-workflow-mods) - dag-workflow: mod do Claude Code para fluxos de trabalho DAG obrigatórios e…
- [joaquinsalinas06/crabbus](https://github.com/joaquinsalinas06/crabbus) - See what every Claude Code subagent is really doing — two-way messaging, tokens…
- [JSungMin/crew-graph](https://github.com/JSungMin/crew-graph) - Claude Code mod: live pane with your agent crew as a tree, plan/doc…
- [kongyo2/context-view](https://github.com/kongyo2/context-view) - A janela de contexto como uma linha acima do prompt, desenhada da forma como o…
- [Kruhlikau/subagent-tuner](https://github.com/Kruhlikau/subagent-tuner) - Claude Code mod: escolhe o modelo e o esforço de raciocínio de cada subagente.
- [KyongSik-Yoon/cc-desktop-mod](https://github.com/KyongSik-Yoon/cc-desktop-mod) - Plugin (mod) de Claude Code que faz a interface de terminal do Claude Code…
- [leonidb/claude-code-mods](https://github.com/leonidb/claude-code-mods) - Não deixe sua atenção se dispersar enquanto espera pela resposta do Claude Code.
- [LudovicLaloux/agent-crew](https://github.com/LudovicLaloux/agent-crew) - Claude Code mod: see your parallel agents as costumed pixel-art Clawds, in a…
- [LupusMalusDeviant/mod-box](https://github.com/LupusMalusDeviant/mod-box) - Fourteen Claude Code mods in one plugin, each switchable, with a window to…
- [m4cd4r4/clear-resume](https://github.com/m4cd4r4/clear-resume) - Um plugin gratuito e de código aberto para Claude Code.
- [marulimo/claude-code-mods](https://github.com/marulimo/claude-code-mods) - Claude Code の Mod 6本（Codex/Devin への依頼、AI 使用率、X 投稿、AI の振り分け、ハッシュタグの流し見、待ち時間の雑談）.
- [michalstrnadel/claude-docket](https://github.com/michalstrnadel/claude-docket) - ◆ A minimal task board inside Claude Code — see what Claude is working on…
- [MitchMedeiros/veneer](https://github.com/MitchMedeiros/veneer) - Take your Claude Code terminal sessions to the next level! Enhanced visuals…
- [modmyclaude/claude-code-mods](https://github.com/modmyclaude/claude-code-mods) - Claude Code mods: curated and tested.
- [muctebadikmen/claude-code-araclari](https://github.com/muctebadikmen/claude-code-araclari) - Claude Code modları: otomatik devir ve ilerleme çubuğu.
- [nonputtipong/claude-code-prompt-enhancer](https://github.com/nonputtipong/claude-code-prompt-enhancer) - ✻ A Claude Code mod that rewrites your rough draft into a clear, project-aware…
- [NotRedFox/NotRedFoxs-Claude-skills](https://github.com/NotRedFox/NotRedFoxs-Claude-skills) - Skills do Claude Code: verificador de fatos para documentos, auditor de código…
- [oobg/claude-code-mods](https://github.com/oobg/claude-code-mods) - Claude Code 입력창과 도구 결과에 기능을 더하는 모드 모음.
- [Plagemes/claude-mods](https://github.com/Plagemes/claude-mods) - 200+ open-source mods for Claude Code: guardrails, status lines, panes and…
- [restante/claudio-tts](https://github.com/restante/claudio-tts) - Make Claude Code talk back 🔊 Local text-to-speech for Claude Code replies…
- [rezzminator/buddy](https://github.com/rezzminator/buddy) - Plugin de companheiro do código Claude: um companheiro ASCII acima do seu…
- [rezzminator/tool-visibility-controller](https://github.com/rezzminator/tool-visibility-controller) - Claude Code plugin for per-agent tool visibility — hide and refuse subagents…
- [roma-vibe/jev-governor](https://github.com/roma-vibe/jev-governor) - Claude Code mod: Jev-guided model/effort routing, verbatim context compaction…
- [Ron-Nefyodov/prompt-library-mod](https://github.com/Ron-Nefyodov/prompt-library-mod) - Save, search and reuse your best Claude Code prompts. Community mod.
- [Ron-Nefyodov/wrapped-mod](https://github.com/Ron-Nefyodov/wrapped-mod) - Your Claude Code year in one shareable card. Community mod.
- [RyanWeera/crab-progress](https://github.com/RyanWeera/crab-progress) - A Claude Code mod: progress bar with a pixel mascot, costumes for every task…
- [simota/claude-mods](https://github.com/simota/claude-mods) - Personal Claude Code mods (function-hook plugins) as one marketplace…
- [Spardutti/claude-mods](https://github.com/Spardutti/claude-mods) - Claude Code mods: live panels and hooks for daily work.
- [tanujarun/it-speaks](https://github.com/tanujarun/it-speaks) - It Speaks: um mod de Claude Code que lê em voz alta as respostas de Claude e…
- [tripolskiydigital/claude-links](https://github.com/tripolskiydigital/claude-links) - A links bar for Claude Desktop.
- [TroyJLorents-GH/mod-squad](https://github.com/TroyJLorents-GH/mod-squad) - Mods do Claude Code: pequenos plugins para painéis ao vivo, roteamento de…
- [valeryia-piatrova/token-hamster](https://github.com/valeryia-piatrova/token-hamster) - 🐹 Mod e plugin do Claude Code: monitor de uso, rastreador de tokens e linha de…
- [varunmoka7/next-steps-autopilot](https://github.com/varunmoka7/next-steps-autopilot) - Shows suggested next prompts above the prompt box.
- [wonjoonSeol-WS/claude-side-insights](https://github.com/wonjoonSeol-WS/claude-side-insights) - Side panel for Claude Code (a mod): checks every question got answered, walks…
- [Xabilimon1/emcc-claude-code-mods](https://github.com/Xabilimon1/emcc-claude-code-mods) - Mods do Claude Code: EMCC (Every Mod Claude Code), uma coleção selecionada e…
- [0hte/glitchdeck](https://github.com/0hte/glitchdeck) - A Claude Code mod that docks a live pane beside your conversation: what Claude…
- [0x5421/plan-progress](https://github.com/0x5421/plan-progress) - A fork of zycck/claude-mods plan-progress: live progress bars for Claude Code…
- [aiob3/claude-grounds](https://github.com/aiob3/claude-grounds) - Claude Code mods that make &quot;done&quot; checkable: the task goal stays on screen and…
- [aiob3/claude-grounds-demo](https://github.com/aiob3/claude-grounds-demo) - Demo for claude-grounds (Claude Code mods): a median() bug with text sort and a…
- [akirachangtw/claude-mods](https://github.com/akirachangtw/claude-mods) - Claude-mods.
- [Akurganow/model-router](https://github.com/Akurganow/model-router) - Claude Code mod: route each subagent to the cheapest Claude model, judged by…
- [Aler1x/claude-cat](https://github.com/Aler1x/claude-cat) - Um gato de braille animado acima do prompt do Claude Code.
- [aloki-alok/omni-cat](https://github.com/aloki-alok/omni-cat) - Um gato em pixel acima do seu prompt do Claude Code que executa uma chamada de…
- [ambervdberg/smartcompact](https://github.com/ambervdberg/smartcompact) - Um mod do Claude Code que escolhe um bom momento para compactar e manter…
- [an80sPWNstar/claude-mods](https://github.com/an80sPWNstar/claude-mods) - Mods Claude para o Claude Code: token-meter.
- [anderson-spider/claude-mods](https://github.com/anderson-spider/claude-mods) - Claude Code plugin marketplace by anderson-spider.
- [andras-gyarmati/claude-quota-band](https://github.com/andras-gyarmati/claude-quota-band) - Claude Code mod: your plan.
- [andras-gyarmati/claude-task-progress](https://github.com/andras-gyarmati/claude-task-progress) - Claude Code mod: progress bars above the prompt for long tasks, background…
- [andrej-kolic/claude-mods](https://github.com/andrej-kolic/claude-mods) - Mods de uso geral para o Claude Code: faixas, painéis, toasts e hooks.
- [anguscyk/claude-mods-task-progress](https://github.com/anguscyk/claude-mods-task-progress) - Shows a progress band above the prompt: a task progress bar with per-task…
- [AntPAllen/claude-mods](https://github.com/AntPAllen/claude-mods)
- [aquarius-wing/copy-session-id](https://github.com/aquarius-wing/copy-session-id) - A Claude Code mod that adds a Copy Session ID button above the prompt.
- [arakx/Claude-Mods](https://github.com/arakx/Claude-Mods) - Mods pour Claude Code.
- [arcnessai/arcdr](https://github.com/arcnessai/arcdr) - herdr mobile &amp; web client that shows what your Claude Code mods report — answer…
- [aseth0/my-claude-mods](https://github.com/aseth0/my-claude-mods) - this is my personal repo of my personals claude-code mods.
- [Ashley-Pettit/villager-hp](https://github.com/Ashley-Pettit/villager-hp) - Seus limites de uso do Claude como um cartão de saúde de aldeão animado, com um…
- [Atanur/deskfit](https://github.com/Atanur/deskfit) - Treinos curtos enquanto Claude trabalha: uma meta diária, sequências…
- [AweGuider/Claude-Context-Control](https://github.com/AweGuider/Claude-Context-Control) - Context Control: a Claude Code mod showing context window fill, what fills it…
- [bahaospanov/skills](https://github.com/bahaospanov/skills) - Mods do Claude Code de Bakhtiyar Ospanov: plugins criados com base em hooks de…
- [benjaminr/nowplaying](https://github.com/benjaminr/nowplaying) - Mod Now Playing para o código Claude: Apple Music e Spotify acima do prompt…
- [berkakkaya/subagents-panel](https://github.com/berkakkaya/subagents-panel) - See what your Claude Code subagents are doing, live, in a side panel.
- [blackironj/claude-mods](https://github.com/blackironj/claude-mods)
- [Br4inergy/claude-hands-off](https://github.com/Br4inergy/claude-hands-off) - Your AI agent can&#x27;t push to a repo, deploy a project or drop a table that isn&#x27;t…
- [Br4inergy/claude-huddle](https://github.com/Br4inergy/claude-huddle) - See when your Claude Code sessions are about to collide in the same repo, and…
- [Br4inergy/claude-loadout](https://github.com/Br4inergy/claude-loadout) - Loadout, the mod manager for Claude Code: audits every mod and every update…
- [broening/claude-mods](https://github.com/broening/claude-mods) - Mods para Claude Code: relógio de cache, raio de impacto, sugestões, lista de…
- [candygoogy/notary](https://github.com/candygoogy/notary) - See what Claude changed, turn by turn. Keep it or send it back.
- [Carismarkus/clowl](https://github.com/Carismarkus/clowl) - Apenas uma coruja para o seu Claude Code.
- [cdeust/claude-mods](https://github.com/cdeust/claude-mods) - Claude Code mods for the ai-architect.tools harness: one concern per mod, state…
- [chinayuren2022-2025/claude-english-coach](https://github.com/chinayuren2022-2025/claude-english-coach) - Claude Code mod: practise English by working with Claude in English only…
- [CiroVilmer/jev-agent-router](https://github.com/CiroVilmer/jev-agent-router) - Claude Code mod that picks the model and effort of every subagent from its task…
- [CoderDayton/vii-mods](https://github.com/CoderDayton/vii-mods) - Claude Code mods for memory, safety and workflow.
- [Crinitys/copy-list](https://github.com/Crinitys/copy-list) - Claude Code mod: a pane of paths and //Next: lines with copy buttons.
- [cskwork/claude-code-mods](https://github.com/cskwork/claude-code-mods) - Claude Code mods: token-weather (context forecast band), blast-radius.
- [danieldeusing/capi-cc-mod](https://github.com/danieldeusing/capi-cc-mod) - Capi: a Claude Code mod that teaches you a language above the prompt, one…
- [DarthSonic/cache-weather-and-pause-resume](https://github.com/DarthSonic/cache-weather-and-pause-resume) - Claude Code mod: a band above the prompt with the prompt-cache countdown…
- [DarthSonic/claude-plugins](https://github.com/DarthSonic/claude-plugins) - Claude Code marketplace darthsonic: a catalog of plugins and mods, each in a…
- [dot-agi/downrange](https://github.com/dot-agi/downrange) - Claude Code mod: background jobs in one view, with progress and ETAs read from…
- [dtakamiya/claude-code-mods](https://github.com/dtakamiya/claude-code-mods) - Claude Code Mods marketplace.
- [edtrackai/claude-code-guardrails-lite](https://github.com/edtrackai/claude-code-guardrails-lite) - Free Claude Code plugin: denies .env reads, git force push and rm -rf on / or…
- [eduojeda/claude-last-answer](https://github.com/eduojeda/claude-last-answer) - Claude Code mod: re-read the agent.
- [eric-liebrecht/claude-mods](https://github.com/eric-liebrecht/claude-mods)
- [fabiopbarbieri/agents-progress](https://github.com/fabiopbarbieri/agents-progress) - Claude Code mod: progress bar above the prompt and a live panel of subagents.
- [flaviorg/claude-mods](https://github.com/flaviorg/claude-mods) - Hub marketplace for my original Claude Code mods: tripwire, canopy, crew…
- [flaviorg/crew](https://github.com/flaviorg/crew) - Claude Code mod: a live panel of the subagents Claude delegates to — model…
- [fllag/claude-mods](https://github.com/fllag/claude-mods) - Mods em teste do time da Hospedin para o Claude Code.
- [grammy-jiang/claude-code-mods-knowledge](https://github.com/grammy-jiang/claude-code-mods-knowledge) - Versioned evidence-backed knowledge base and cross-agent skills for Claude Code…
- [gwarf/claude-plugins](https://github.com/gwarf/claude-plugins) - Claude Code mods by Baptiste Grenier: a plugin marketplace.
- [h1048576/claude-mods](https://github.com/h1048576/claude-mods) - Claude Code mods - show-mode plugin.
- [HakanKorkz/korkz-claude-mod](https://github.com/HakanKorkz/korkz-claude-mod) - Claude Code için modlar: maliyet şeridi, tehlike kalkanı, Türkçe cevap, iş…
- [hashswingingslasher/model-hint](https://github.com/hashswingingslasher/model-hint) - Claude Code mod: suggests haiku, sonnet or opus for the task you are typing…
- [hb03/claude-mods](https://github.com/hb03/claude-mods) - Deutschsprachige Mods für Claude Code: Kontext/Cache-Hinweise, offene Punkte…
- [Hekzory/spend-meter](https://github.com/Hekzory/spend-meter) - Um medidor de gastos ao vivo para o Claude Code: o custo da sessão com…
- [helenkwok/rustgis-tui](https://github.com/helenkwok/rustgis-tui) - A terminal UI for RustGIS, and a Claude Code pane you and Claude drive…
- [HoyngM/claude-mods](https://github.com/HoyngM/claude-mods) - Mods for Claude Code.
- [HuliLulu46/cc-commit-command](https://github.com/HuliLulu46/cc-commit-command)
- [HuliLulu46/cc-effort-switch](https://github.com/HuliLulu46/cc-effort-switch)
- [HuliLulu46/cc-prompt-polish](https://github.com/HuliLulu46/cc-prompt-polish)
- [HuliLulu46/pending-decisions](https://github.com/HuliLulu46/pending-decisions)
- [humvnpvrvdox777/NextSteps](https://github.com/humvnpvrvdox777/NextSteps) - Claude Code mod: three next steps after each answer, in any language, with an…
- [Huuuuung/think-meter](https://github.com/Huuuuung/think-meter) - Mod de código do Claude: quanto tempo cada resposta levou, quanto tempo Claude…
- [huynl-96/claude-mods](https://github.com/huynl-96/claude-mods) - Claude Code mods: streamer-mode hides private panes, bands and the status line…
- [isandrel/redact-restore](https://github.com/isandrel/redact-restore) - Reversible redaction for Claude Code: the model sees placeholders, you and your…
- [iuliandita/mods](https://github.com/iuliandita/mods) - Claude Code mods you can install one at a time.
- [iyiob96/Context-Mod-Companion](https://github.com/iyiob96/Context-Mod-Companion) - Claude Code mod: context window band with RTK savings and a pixel Yemeni…
- [jasoncai0/claude-session-hud](https://github.com/jasoncai0/claude-session-hud) - Claude Code mod: rate-limit usage, Codeup MRs and the session.
- [jepperip/claude-session-todo](https://github.com/jepperip/claude-session-todo) - Claude Code mod: a live session todo pane the agent keeps current.
- [jessetsai1024/claude-ctx-panel](https://github.com/jessetsai1024/claude-ctx-panel) - Painel de uso do contexto na barra lateral: total, categorias, crescimento por…
- [jessetsai1024/claude-files](https://github.com/jessetsai1024/claude-files) - Lista de arquivos na barra lateral: quais arquivos foram criados, modificados…
- [jessetsai1024/claude-maomao](https://github.com/jessetsai1024/claude-maomao) - 毛毛, um coelho holandês anão preto e branco em estilo 8-bit, corre e pula acima…
- [jessetsai1024/claude-prompts](https://github.com/jessetsai1024/claude-prompts) - A seção “O que eu perguntei” na barra lateral: cada frase que o usuário digitou…
- [jessetsai1024/claude-timeline](https://github.com/jessetsai1024/claude-timeline) - Linha do tempo na barra lateral: onde o tempo desta rodada foi gasto.
- [jessetsai1024/claude-tokens](https://github.com/jessetsai1024/claude-tokens) - Movimentação de tokens na barra lateral: quantos tokens a conversa principal…
- [jessetsai1024/claude-whisper](https://github.com/jessetsai1024/claude-whisper) - O “confessionário honesto” do claude code: após responder em cada rodada…
- [jjayakumar-gif/compass-claude-mods](https://github.com/jjayakumar-gif/compass-claude-mods)
- [joaopasbento/claude-mods](https://github.com/joaopasbento/claude-mods) - Claude Code mods: token-weather, a live forecast of the context window above…
- [jsc2304/great-question](https://github.com/jsc2304/great-question) - Claude Code side panel: the questions most likely to come up before a pitch…
- [kad1r/claude-mods](https://github.com/kad1r/claude-mods)
- [KaiC5504/clawd-bar](https://github.com/KaiC5504/clawd-bar) - Clawd vive em uma faixa acima do prompt do Claude Code: encena a sessão, mostra…
- [kajidog/cc-mods-tts](https://github.com/kajidog/cc-mods-tts) - Um mod que lê em voz alta as respostas e notificações do Claude Code usando…
- [kakwok/claude-mods](https://github.com/kakwok/claude-mods)
- [kiankhooban/open-paths](https://github.com/kiankhooban/open-paths) - Click a file path in Claude Code and the file opens in its app: Word, Preview…
- [Kiyliy/claude-code-tps](https://github.com/Kiyliy/claude-code-tps) - Claude Code mod: status line showing output speed (tps), TTFT, total time and…
- [Koder-SpA/claude-mods](https://github.com/Koder-SpA/claude-mods) - Claude Code plugins by Koder SpA — real-time token cost, context and rate-limit…
- [krishna-goutham-tls/cc-mods](https://github.com/krishna-goutham-tls/cc-mods) - Two Claude Code mods: folio, a file pane beside the chat, and tint, a restyle…
- [kuzmany/cc-model-effort-switcher](https://github.com/kuzmany/cc-model-effort-switcher) - Switch Claude Code model and reasoning effort in one command: /m opus high.
- [leonardogub-singular/claude-repo-changes](https://github.com/leonardogub-singular/claude-repo-changes) - Claude Code mod: git changes and diffs for every repo and worktree in a…
- [Lerma4/claude-code-mods](https://github.com/Lerma4/claude-code-mods) - A collection of mods for Claude Code.
- [levy-n/claude-code-mods](https://github.com/levy-n/claude-code-mods) - Claude Code mods for long sessions: context-handoff.
- [lijingwu2026/claude-code-plan-tracker](https://github.com/lijingwu2026/claude-code-plan-tracker) - A live board of your approved plan: which steps are done, running, blocked or…
- [Lingfar/claude-code-mods](https://github.com/Lingfar/claude-code-mods) - Personal Claude Code mods: plan usage footer and background tasks band.
- [Lucas-CX/awesome-claude-mods](https://github.com/Lucas-CX/awesome-claude-mods) - Um guia de Mods do Claude Code organizado pela comunidade: casos de uso…
- [M-i-k-e-l/agent-state](https://github.com/M-i-k-e-l/agent-state) - Um mod do Claude Code que mostra o que Claude está fazendo no subtítulo da aba…
- [MagnusPladsen/claude-mods](https://github.com/MagnusPladsen/claude-mods) - Personal global Claude Code mods.
- [Mariator-pro/claude-mod-statusline](https://github.com/Mariator-pro/claude-mod-statusline) - Claude Code mod that shows model, context, prompt cache countdown and 5h/7d…
- [migmorales22/claude-stock-ticker](https://github.com/migmorales22/claude-stock-ticker) - A Claude Code mod: /stock AAPL keeps one stock.
- [miiraheart/marginalia](https://github.com/miiraheart/marginalia) - Claude Code mod: select text in the conversation, then quote it into your…
- [minhtran3124/cc-ste-mod](https://github.com/minhtran3124/cc-ste-mod) - Claude Code mod that rewrites your prompt in ASD-STE100 Simplified Technical…
- [Mistakey/anvil](https://github.com/Mistakey/anvil) - Claude Code mod: keeps the prompt cache warm while you.
- [MoonZhe/usage-band](https://github.com/MoonZhe/usage-band) - Claude Code mod: usage band above the prompt with 5h/7d limits, tokens, context…
- [mreedr/gh-linear-parse-mod](https://github.com/mreedr/gh-linear-parse-mod) - Claude Code mod: GitHub PR and Linear links band above the prompt.
- [mrsono0/ctx-footer](https://github.com/mrsono0/ctx-footer) - Claude Code mod: context window usage in the prompt footer mode slot.
- [mtmtian/cc-mods](https://github.com/mtmtian/cc-mods) - Claude Code mods (function-hook plugins) forked from other authors, kept in one…
- [muellerei/enable-todo-tools](https://github.com/muellerei/enable-todo-tools) - Mod do Claude Code que reativa as ferramentas de tarefas pendentes para modelos…
- [muellerei/sweet-spot](https://github.com/muellerei/sweet-spot) - Mod do Claude Code que espera uma pausa segura e então transfere sua sessão ou…
- [muellerei/task-line](https://github.com/muellerei/task-line) - Mod do Claude Code: uma linha por tarefa acima do prompt com a tarefa atual…
- [mukuro696-dev/guard-and-band-for-claude-code](https://github.com/mukuro696-dev/guard-and-band-for-claude-code) - Small self-made Claude Code mods: guard-a.
- [mvacoimbra/claude-mods-hub](https://github.com/mvacoimbra/claude-mods-hub) - One /mods pane for every installed Claude Code mod.
- [nachtgold/claude-code-connect-four](https://github.com/nachtgold/claude-code-connect-four) - Jogue Connect Four contra uma AI dentro do Claude Code (/connect-four).
- [Nagato-Yuzuru/crabarium](https://github.com/Nagato-Yuzuru/crabarium) - A Claude Code mod: a pane that shows the main session and its subagents, with…
- [naoanao/agent-cross-check](https://github.com/naoanao/agent-cross-check) - Mod de Claude Code: quando outro agente de programação faz commit no seu…
- [naoanao/shared-repo-guard](https://github.com/naoanao/shared-repo-guard) - Mod de Claude Code para repositórios compartilhados por vários agentes de IA…
- [nasmarr/claude-mods](https://github.com/nasmarr/claude-mods) - A small catalog of Claude Code mods.
- [natansalvadorligabo/claude-usage-meter](https://github.com/natansalvadorligabo/claude-usage-meter) - A Claude Code mod that shows context, 5-hour session and weekly usage on the…
- [NathapolDev/al-status-line](https://github.com/NathapolDev/al-status-line) - AL Status for Claude Code mods.
- [necobit/claude-lupin-title](https://github.com/necobit/claude-lupin-title) - A Claude Code mod: typewriter clacks, a full-screen title card and excuses with…
- [nemokoala/claude-mods](https://github.com/nemokoala/claude-mods) - Claude Code mods: usage gauges and a collapsible git graph.
- [niksavis/handily](https://github.com/niksavis/handily) - Mods do Claude Code que mostram seus itens de trabalho, tarefas e sessões, para…
- [nxhung1610/claude-odometer](https://github.com/nxhung1610/claude-odometer) - Claude Code mod that shows your 5-hour and 7-day usage limits right under the…
- [ohade/claude-mods](https://github.com/ohade/claude-mods) - Claude Code mods: image thumbnails and the status line.
- [oscar-guggiana-neto-neocol/claude-mods](https://github.com/oscar-guggiana-neto-neocol/claude-mods)
- [Para-FR/claude-code-mods-fr](https://github.com/Para-FR/claude-code-mods-fr) - Dois Mods do Claude para o Claude Code: guarda-corpo.
- [patrick-lai/claude-fish-stack-mod](https://github.com/patrick-lai/claude-fish-stack-mod) - fishStack: um Claude Code mod. Worktrees permanentes com início somente…
- [pekala/linear-review-link](https://github.com/pekala/linear-review-link) - Claude Code mod: the current branch.
- [PershinIlya/Claude-Code-Mods](https://github.com/PershinIlya/Claude-Code-Mods)
- [PeterTing/claude-mod](https://github.com/PeterTing/claude-mod) - Hand-made and curated Claude Code mods: panes, status lines, slash commands…
- [philarete173/claude_mods](https://github.com/philarete173/claude_mods) - Painel lateral ao vivo de estatísticas da sessão para a aba Code do aplicativo…
- [PickleBoxer/pickle](https://github.com/PickleBoxer/pickle) - pickle for Claude Code: language-agnostic engineering playbooks and principles…
- [pnam16/claude-mods](https://github.com/pnam16/claude-mods) - Claude Code mods, kept as the ame-mods marketplace.
- [pradyb/claude-mods](https://github.com/pradyb/claude-mods) - Mods for Claude Code: safety-guard blocks destructive commands and secret-file…
- [pstahel/token-weather-claude-code-mod](https://github.com/pstahel/token-weather-claude-code-mod) - A live dashboard of your context window and prompt cache above the Claude Code…
- [qr1x55/Detaly-Claude-Mod](https://github.com/qr1x55/Detaly-Claude-Mod) - Live progress bars above the prompt for long jobs in Claude Code.
- [ramonfabrega/mods](https://github.com/ramonfabrega/mods) - Claude Code mods: hooks modules that change the interface.
- [reedchan7/claude-mods-pulse](https://github.com/reedchan7/claude-mods-pulse) - Pulse: live TTFT, tok/s, prompt-cache hit rate and usage left in Claude Code.
- [Risdon8/push-ups](https://github.com/Risdon8/push-ups) - Mod do Claude Code: flexões para fazer enquanto Claude trabalha. Sem tokens.
- [RobGruhl/claude-mod-learnings](https://github.com/RobGruhl/claude-mod-learnings) - Hook Chain: um guia de campo para Claude Code mods, de ELI5 a engenharia de…
- [Rohitp/claude-mods](https://github.com/Rohitp/claude-mods) - Mods for claude code.
- [rolottr/claude-mod-meatproxy](https://github.com/rolottr/claude-mod-meatproxy) - Claude Code mod that shows drafts in a side pane, where you copy them as rich…
- [Ron-Nefyodov/pet-mod](https://github.com/Ron-Nefyodov/pet-mod) - A tiny terminal pet that lives on your Claude Code sessions. Community mod.
- [saadk408/stepline](https://github.com/saadk408/stepline) - Mod do Claude Code: transforma o plano que você aprova no modo de planejamento…
- [saksham10arora-dotcom/awesome-claude-mods](https://github.com/saksham10arora-dotcom/awesome-claude-mods) - Uma lista selecionada de mods do Claude Code.
- [saksham10arora-dotcom/claude-frugal](https://github.com/saksham10arora-dotcom/claude-frugal) - Modo sem custo: os agentes auxiliares rodam no Haiku, e arquivos grandes e logs…
- [saksham10arora-dotcom/claude-lofi](https://github.com/saksham10arora-dotcom/claude-lofi) - Uma trilha sonora lofi que acompanha a sessão: calma, foco, fluxo, além de…
- [saksham10arora-dotcom/claude-teach-me](https://github.com/saksham10arora-dotcom/claude-teach-me) - Aprenda enquanto Claude programa: após um turno que alterou o código, uma…
- [saksham10arora-dotcom/claude-vhs](https://github.com/saksham10arora-dotcom/claude-vhs) - Uma gravação de cada edição feita por Claude: reproduza cada alteração sendo…
- [samykantari/secret-redact](https://github.com/samykantari/secret-redact) - Claude Code mod that masks secrets in tool outputs before Claude reads them.
- [schudarin/chudarin-context-mod](https://github.com/schudarin/chudarin-context-mod) - A Claude Code mod: a side panel that shows what fills your context, how much of…
- [sergeiwallace/beads-ui](https://github.com/sergeiwallace/beads-ui) - Beads task manager UI: a Claude Code mod for the TUI, an MCP UI app for Claude…
- [sergeiwallace/doc-editor](https://github.com/sergeiwallace/doc-editor) - A doc viewer and editor inside the Claude Code TUI, built as a Claude Code mod…
- [sgript-labs/claude-mods](https://github.com/sgript-labs/claude-mods) - Claude Code mods from Sgript: Sprout, a pixel creature above the prompt, plus…
- [ShadowDog007/claude-mods](https://github.com/ShadowDog007/claude-mods)
- [ShagnikPal123/mission-control](https://github.com/ShagnikPal123/mission-control) - Claude Code mod: context and usage meters, auto-resume, model router, agent…
- [shhac/claude-mods](https://github.com/shhac/claude-mods) - Mods for Claude Code.
- [shichang4fun/claude-mods](https://github.com/shichang4fun/claude-mods) - Personal Claude Code mods, published as a plugin marketplace.
- [sidhantunnithan/jindan-cc-marketplace](https://github.com/sidhantunnithan/jindan-cc-marketplace) - Personal Claude Code mods.
- [sinozu/claude-code-mods](https://github.com/sinozu/claude-code-mods)
- [SipengXie2024/claude-mods](https://github.com/SipengXie2024/claude-mods)
- [SJvaca30/mulgogi-mods](https://github.com/SJvaca30/mulgogi-mods) - 한국어 화면의 Claude Code mod 모음: clickbar(입력창 위 버튼·상태 줄, 명령 팔레트), session-tracker.
- [skaterino/claude-mods](https://github.com/skaterino/claude-mods) - Claude-Code-Mods: Verbrauchs-Statuszeile mit Auto-Neustart (verbrauch) und…
- [StanislavKozachenko/claude-mods](https://github.com/StanislavKozachenko/claude-mods) - A collection of Claude Code mods: TypeScript function hooks, shipped as a…
- [steven-ngle/blade-of-commits](https://github.com/steven-ngle/blade-of-commits) - Mensagens de commit com um clique para Claude Code com uma Malenia dançante em…
- [sushant-kum/ccstatus](https://github.com/sushant-kum/ccstatus) - A configurable status bar for Claude Code — band, native status line, pane, and…
- [Tanish-Dev/claude-usage-band](https://github.com/Tanish-Dev/claude-usage-band) - Clawd Meter — uma modificação do Claude Code que mostra o uso do seu plano…
- [tanmen/claude-tanmen-plugins](https://github.com/tanmen/claude-tanmen-plugins) - Mods não oficiais do Claude Code por tanmen (marketplace: tanmen).
- [TheBabaYaga/claude-session-flow](https://github.com/TheBabaYaga/claude-session-flow) - Um mod do Claude Code que mostra a sessão atual em um painel: cada prompt, o…
- [theishandubey/claude-mods](https://github.com/theishandubey/claude-mods) - Um marketplace de plugins do Claude Code de mods: plugins function-hooks que…
- [thitiwats/claude-mods](https://github.com/thitiwats/claude-mods) - Claude Code mods, published as a plugin marketplace.
- [ThomasTartrau/charts](https://github.com/ThomasTartrau/charts) - Claude Code mod that renders vega-lite, mermaid and dot code blocks as real…
- [tinkybeatz/tinky-claude-mods](https://github.com/tinkybeatz/tinky-claude-mods) - Claude Code mods: interface and behaviour plugins built on function hooks.
- [tndavidson/claude-mods](https://github.com/tndavidson/claude-mods) - Mods for Claude Code: next-step prompt suggestions and a task progress bar…
- [toml0006/claude-session-stats](https://github.com/toml0006/claude-session-stats) - Claude Code mod: live pane of your session.
- [Ty-Stev/ty-mods](https://github.com/Ty-Stev/ty-mods) - Ty.
- [tyastonotaufiq/claude-mods](https://github.com/tyastonotaufiq/claude-mods)
- [VAlux/claude-session-progress](https://github.com/VAlux/claude-session-progress) - Mod do Claude Code: faixa de progresso animada e resumo de conclusão para…
- [Vansitha/clawd-watch](https://github.com/Vansitha/clawd-watch) - Três pequenos mods de Claude Code: veja quando seus subagentes terminarão…
- [varunmoka7/layman](https://github.com/varunmoka7/layman) - Diga &quot;Estou perdido&quot; e Claude explicará novamente sua última resposta em…
- [varunmoka7/side-chat](https://github.com/varunmoka7/side-chat) - Faça uma pergunta paralela a Claude em um painel ao lado do seu trabalho.
- [vinicius-sandes/crabhud](https://github.com/vinicius-sandes/crabhud) - A Claude Code mod: a crab that shows what Claude is doing, a progress bar for…
- [vlle/job-hunt-cc](https://github.com/vlle/job-hunt-cc) - A Claude Code mod that lets you find job and tailor your resume(s).
- [whilestevego/claude-mods](https://github.com/whilestevego/claude-mods) - Claude Code mods: context bar, rate-limit gauges, session ID, tab titles, turn…
- [wjsekrud/motive-mem](https://github.com/wjsekrud/motive-mem) - Claude Code mod: after every turn, a separate model reviews the change against…
- [wukonigcom/quanta-costa](https://github.com/wukonigcom/quanta-costa) - 🧾 Plugin do Claude Code: seus limites de uso do Claude Pro/Max com previsão de…
- [xinhuagu/oh-my-claude-mods](https://github.com/xinhuagu/oh-my-claude-mods) - Mods para o Claude Code. agent-crew: acompanhe seus subagentes trabalhando como…
- [yyh-001/dsh-supermarket](https://github.com/yyh-001/dsh-supermarket) - 超级市场：面向 AI 的 DSH 多市场插件，统一发现、管理与使用 Skills、MCP、Claude Mods、整合包和 Agent 预设.
- [zcharef/session-topic](https://github.com/zcharef/session-topic) - Claude Code mod that names each session after what it is about, and shows the…
- [zexion7873/usage-band](https://github.com/zexion7873/usage-band) - Always-on band above the Claude Code prompt: context fill and rate-limit…
- [zhuobichen/zhaowen-claudemod](https://github.com/zhuobichen/zhaowen-claudemod) - 我自用的 Claude Code mod 合集（function hooks）：以 marketplace 形式分发，/plugin install 装.
- [ziedgithub/claude-code-mods](https://github.com/ziedgithub/claude-code-mods)
- [Ztubben/claude-code-mods](https://github.com/Ztubben/claude-code-mods) - Mods and other artifacts for Claude Code.
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
- [awesomezun/claude-statusline](https://github.com/awesomezun/claude-statusline) - An aesthetic statusline for Claude Code by awesomezun.
- [JohnnyVizz/claude-kit](https://github.com/JohnnyVizz/claude-kit) - Skills e mods públicos para Claude Code.
- [ilia-pluzhnikov/claude-code-statusline](https://github.com/ilia-pluzhnikov/claude-code-statusline) - A feature-rich, dependency-free Node.js statusline for Claude Code with model…
- [escapeboy/claude-code-kit](https://github.com/escapeboy/claude-code-kit) - Skills, mods, subagentes, hooks, comandos slash e guias para Claude Code…
- [mvalentsev/awesome-free-ai-coding](https://github.com/mvalentsev/awesome-free-ai-coding) - 📡 LLM APIs e agentes de programação gratuitos e legais — atualizados…
- [congmnguyen/claude-code-wsl2-setup](https://github.com/congmnguyen/claude-code-wsl2-setup) - Guides and scripts for Claude Code on WSL2: screenshot paste, Windows…
- [arturogarrido/claudinho](https://github.com/arturogarrido/claudinho) - ⚽ Placar ao vivo de futebol, jogos e classificações da competição que você…
- [johncattrall/keymap-ai](https://github.com/johncattrall/keymap-ai) - Agent Skill que transforma seu agente de programação em especialista em…
- [benabraham/claude-code-status-line](https://github.com/benabraham/claude-code-status-line) - Statusline script for Claude Code CLI – shows context and quota usage, model…
- [ashafizullah/claude-code-muslim-mods](https://github.com/ashafizullah/claude-code-muslim-mods) - Horários de oração, data Hijri, adhkar, ayah diária, jejum sunnah, Ramadan…
- [philoserf/claude-code-config](https://github.com/philoserf/claude-code-config) - Configuração pessoal do Claude Code versionada dentro de ~/.claude — agentes…
- [rlaope/deepseek-bot](https://github.com/rlaope/deepseek-bot) - DeepSeek Harness gonna be your personal agent, a self-hosted AI teammate that…
- [hoobnn/hoobnn-agent-mods](https://github.com/hoobnn/hoobnn-agent-mods) - Coleção de plugins para Claude Code, pi e DeepSeek Harness: HUD da barra de…
- [pierrebelin/claude-code-toolkit](https://github.com/pierrebelin/claude-code-toolkit) - Kit de ferramentas portátil do Claude Code para DDD/Arquitetura Limpa em .NET…
- [FlorinI/Florians-Claude-Code-Kit](https://github.com/FlorinI/Florians-Claude-Code-Kit) - Cross-platform Node status line for Claude Code, plus /handover…
- [jcdendrite/claude-config](https://github.com/jcdendrite/claude-config) - Configuração global portátil do Claude Code: habilidades personalizadas, hooks…
- [manson341349-beep/claude-desktop-mods](https://github.com/manson341349-beep/claude-desktop-mods) - Mods não oficiais para a aba Code do Claude Desktop — usage-pet: uma faixa de…
- [mutlumehmet/claude-plugins](https://github.com/mutlumehmet/claude-plugins) - Plugins do Claude Code que uso todos os dias: skills e mods, organizados para…
- [alpadalar/ccinfobar](https://github.com/alpadalar/ccinfobar) - Uma linha de status personalizável para Claude Code com um editor de arrastar e…
- [MindLab-Research/dsh-generative-ui](https://github.com/MindLab-Research/dsh-generative-ui) - Generative UI for DeepSeek Harness — the agent writes TSX and the web UI…
- [will-pagane/claude-superdev-harness](https://github.com/will-pagane/claude-superdev-harness) - Minha config pessoal do Claude Code — CLAUDE.md global, statusline custom…
- [cativo23/lumira](https://github.com/cativo23/lumira) - Real-time statusline HUD for Claude Code and Qwen Code.
- [darthmolen/hytale-claude-code-marketplace](https://github.com/darthmolen/hytale-claude-code-marketplace) - Marketplace de plugins e skills do Claude Code para facilitar mods do jogo…
- [GerardoFC8/claude-subagent-statusline](https://github.com/GerardoFC8/claude-subagent-statusline) - Real-time sub-agent delegation tracking in your Claude Code statusline.
- [hopp1395/cc-outline](https://github.com/hopp1395/cc-outline) - Visualizador de painéis divididos para o Claude Code no Windows Terminal e…
- [romnycristopher/claude-am-mods](https://github.com/romnycristopher/claude-am-mods) - Repositório de mods Awesome Media para Claude Code.
- [fbincon/claude-code-statusline](https://github.com/fbincon/claude-code-statusline) - Configurable Claude Code status line for Linux, WSL, Windows and macOS, with…
- [zach-source/claude-factory](https://github.com/zach-source/claude-factory) - Definable software factories for Claude Code on herdr: xstate station graphs, a…
- [ahwenu/claude-cafe-mods](https://github.com/ahwenu/claude-cafe-mods) - ☕ Claude Code の Mod 集。cafe-files: 喫茶店風のファイルペイン（/files）.
- [carterptull/ampline-claude](https://github.com/carterptull/ampline-claude) - Uma statusline amplificada, com gradação de cores e sem dependências para o…
- [daydeda/claude-code-statusline](https://github.com/daydeda/claude-code-statusline) - A colorful, compact 4-line status line for Claude Code: effort, folder, git…
- [FukKwang/claude-statusline](https://github.com/FukKwang/claude-statusline) - Colorful Claude Code status line: plan limits, context, cost and tokens.
- [kgdemir/claude-agentic-os](https://github.com/kgdemir/claude-agentic-os) - Claude Agentic OS: portable Claude Code setup — global rules, plugin set…
- [magacho/claude-code-statusbar](https://github.com/magacho/claude-code-statusbar) - Statusline de duas linhas para o Claude Code: diretório, branch, modelo, modo…
- [nrzz/claude-code-team-sync](https://github.com/nrzz/claude-code-team-sync) - Share Claude Code sessions, notes and team context with coworkers: hand over…
- [ta17eee/claude-code-statusline](https://github.com/ta17eee/claude-code-statusline) - モデル・コンテキストウィンドウ・レートリミット・git情報を表示する、Claude Codeのカスタムステータスライン.
- [tc3oliver/claude-team-kit](https://github.com/tc3oliver/claude-team-kit) - Equipes de agentes nativas. Sob controle.
- [YoanWai/claude-code-statusline](https://github.com/YoanWai/claude-code-statusline) - Claude Code status line with context bar, rate limits, git, PRs, and a rotating…
- [0hte/claude-statusline](https://github.com/0hte/claude-statusline) - Two-line status line for Claude Code: context gauge, prompt cache countdown…
- [31c0c3/claude-statusline](https://github.com/31c0c3/claude-statusline) - One-line Claude Code status line in bash and jq: context, cache, limits, cost.
- [aaltw/claude-code-statusline](https://github.com/aaltw/claude-code-statusline) - Catppuccin Mocha powerline statusline for Claude Code — model, tokens, context…
- [akhilnalliboina/claude-usage-statusline](https://github.com/akhilnalliboina/claude-usage-statusline) - Claude Code usage status line for macOS and Linux, packaged as a herdr…
- [alanmarcero/claude-statusline-arcade-roulette](https://github.com/alanmarcero/claude-statusline-arcade-roulette) - Claude Code status line that deals each session one of ten classic arcade games.
- [bunderlog/claude-plugins](https://github.com/bunderlog/claude-plugins) - Claude Code plugin marketplace with baloo: skills, an agent that verifies…
- [ctfbio/claude-code-statusline](https://github.com/ctfbio/claude-code-statusline) - Statusline do Claude Code de nível profissional: duração da sessão, custo em…
- [drewkhouryorg/claude-statusline](https://github.com/drewkhouryorg/claude-statusline) - Uma linha de status para o Claude Code: contexto, limites e o ritmo da semana…
- [fabifont/claude-statusline](https://github.com/fabifont/claude-statusline) - Minimal offline Claude Code status line written in Rust.
- [Fibonach0/claude-code-gadgets-linux](https://github.com/Fibonach0/claude-code-gadgets-linux) - Accesorios para Claude Code en Linux (Debian/Ubuntu): % de uso en la bandeja…
- [hawkymisc/claude-plugins](https://github.com/hawkymisc/claude-plugins) - Hawkie.
- [hieuvo/claude-imgview](https://github.com/hieuvo/claude-imgview) - Visualize imagens dentro do Claude Code: passe o cursor sobre um chip abaixo de…
- [IchiSieben/claude-kit](https://github.com/IchiSieben/claude-kit) - An operating kit for Claude Code: routing by lane, subagents, a review gate…
- [izahamyatim/claude-plugin-fizzy](https://github.com/izahamyatim/claude-plugin-fizzy) - 🚀 Sincronize as tarefas de Claude com o Fizzy.do para obter visibilidade da…
- [jamesyoung-dev/claude-cache-countdown](https://github.com/jamesyoung-dev/claude-cache-countdown) - Keeps claude_statusline_plus.
- [jaszerr/Claude-Statusline](https://github.com/jaszerr/Claude-Statusline) - Minimal, extensible status line for Claude Code.
- [jdmalter/claude-code-statusline](https://github.com/jdmalter/claude-code-statusline) - A muted three-line status line for Claude Code, in bash for Git Bash on Windows.
- [kouui/magic-claude-code-plugin](https://github.com/kouui/magic-claude-code-plugin) - awesome claude code plugin marketplace: skills, mods, ...
- [LeonJoeeee/DevStandard-ClaudeCode](https://github.com/LeonJoeeee/DevStandard-ClaudeCode) - The GitHub flow, extended to agent teams — a Claude Code plugin for developing…
- [lucasmm96/claude-statusline](https://github.com/lucasmm96/claude-statusline) - Hook de statusline do Claude Code — rastreia o uso de tokens e o contexto entre…
- [MBaranekTech/claude-caveman-statusline](https://github.com/MBaranekTech/claude-caveman-statusline) - 🪨 Claude Code status line with caveman badge and remaining usage progress bars.
- [mderiano/claude-cockpit](https://github.com/mderiano/claude-cockpit) - Cockpit for Claude Code: a live, colorful pane showing commands &amp; output, file…
- [mesix971/mods-claude](https://github.com/mesix971/mods-claude) - Clawd, le compagnon en pixel art de Claude Code, et atelier, le garde-fou du…
- [milan44i/claude-setup](https://github.com/milan44i/claude-setup) - An installable Claude Code setup: self-healing TypeScript hook…
- [mileschintw/claude-cache-timer](https://github.com/mileschintw/claude-cache-timer) - Prompt cache countdown and auto-compact for Claude Code.
- [mr-pmillz/claude-code-pmillz-statusline](https://github.com/mr-pmillz/claude-code-pmillz-statusline) - a status line variant for claude code that shows useful info.
- [msinclair-sudo/claude-code-setup](https://github.com/msinclair-sudo/claude-code-setup) - Claude Code environment installer: skills, statusline, hooks, permissions, and…
- [ni-c/claude-usage-statusline](https://github.com/ni-c/claude-usage-statusline) - Claude Code status line with rate-limit usage and reset countdowns, git branch…
- [robinalexandre/claude-code-kit](https://github.com/robinalexandre/claude-code-kit) - Skills, mods, hooks and a status line for Claude Code, plus a sync engine for…
- [Rubio-Enterprises/claude-statusline](https://github.com/Rubio-Enterprises/claude-statusline) - Linha de status personalizada do Claude Code.
- [spyrad/claude-code-statusline](https://github.com/spyrad/claude-code-statusline) - A status line for Claude Code on Windows: model, repo and branch, rate-limit…
- [stelsoft/claude-code-statusline](https://github.com/stelsoft/claude-code-statusline) - Zero-dependency bash statusline for Claude Code: context usage bar + 5h/7d…
- [tetthews/claude-uso-tokens](https://github.com/tetthews/claude-uso-tokens) - Mod pro Claude Code: faixa colorida com o uso do limite (5h e semana) e a…
- [tumuyijiao114514/claude-pulse](https://github.com/tumuyijiao114514/claude-pulse) - ⚡ StatusLine Multi-Protocolo Universal, Autoaprendizado de Contexto e Plugin…
- [Winn-Gaoti-Studio/claude-code-statusline](https://github.com/Winn-Gaoti-Studio/claude-code-statusline) - A Claude Code statusline with gradient progress bars, color-graded session…
- [YoniYon00/claude-feedback-rings](https://github.com/YoniYon00/claude-feedback-rings) - Detector de deterioração de contexto 2026 — Monitor proativo de memória de IA e…
- [ZeyuSi-2099/claude-code-statusline](https://github.com/ZeyuSi-2099/claude-code-statusline) - Claude Code custom statusline (macOS): cwd/git/model/effort/ctx/5h/wk in one…
- [zhuyansen/awesome-claude-code-hooks](https://github.com/zhuyansen/awesome-claude-code-hooks) - Hooks, subagentes e linhas de status do Claude Code: coleções e ferramentas de…
- [ratelworks/token-horse](https://github.com/ratelworks/token-horse) - Token usage reactive horse pet for Claude Code statuslines and Codex CLI…
- [ishuagrawal/clawdhouse](https://github.com/ishuagrawal/clawdhouse) - Mods para Claude Code: painéis, faixas e companheiros baseados em hooks de…
- [ashishsk93/baton-mods](https://github.com/ashishsk93/baton-mods) - Passe tarefas entre suas sessões do Claude Code.
- [charlie947/mod-maker](https://github.com/charlie947/mod-maker) - Mod Maker: encontre o que você pede ao Claude Code repetidamente e transforme…
- [lahoramaker/mods-mcp](https://github.com/lahoramaker/mods-mcp) - Isto em um servidor MCP para controlar o MODS, a ferramenta modular…
- [Rimcat-JA/translate-ck3-mods](https://github.com/Rimcat-JA/translate-ck3-mods) - Skill de Codex e Claude Code para traduzir mods de CK3 com um LLM local.
- [sTomerG/agent-kit](https://github.com/sTomerG/agent-kit) - Mods de código aberto e outras extensões para Claude Code.
- [GregoryHo/cc-pulseline](https://github.com/GregoryHo/cc-pulseline) - High-performance Claude Code statusline with observability.
- [Isllanrx/status_cli](https://github.com/Isllanrx/status_cli) - Status line in Rust for Claude Code, Codex CLI and Antigravity CLI: usage…

</details>

<a id="dsh-cordis"></a>

## Ecossistemas de plugins do DSH e do Cordis

DeepSeek Harness e Cordis chegam ao mesmo lugar por uma direção diferente: para eles, o plugin é o mecanismo de modificação; portanto, um plugin lá equivale a um mod aqui.

<details>
<summary>🧵 <b><a href="https://github.com/deepseek-ai/deepseek-harness">deepseek-ai/deepseek-harness</a></b> · ⭐250275 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **250275** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-agents` · `cordis` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ruvnet/ruflo">ruvnet/ruflo</a></b> · ⭐74863 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **74863**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agentic-ai` · `agentic-framework` · `agentic-workflow` · `agents` · `ai-agents` · `ai-assistant` · `ai-skills` · `autonomous-agents`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/86b2691275e30a26.jpg" width="100%" alt="ruvnet/ruflo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ruvnet--ruflo/2ca82c9c9a7fca31.gif" width="100%" alt="ruvnet/ruflo animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ccch1mneyyy/dsh-TUI">ccch1mneyyy/dsh-TUI</a></b> · ⭐4631 · TypeScript · 👁️ observed · 0 天</summary>

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
| Stars        | **4631**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-12 |

🏷 `claude-code` · `coding-agent` · `deepseek` · `deepseek-harness` · `dsh-plugin` · `ink` · `react` · `terminal`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/hashgraph-online/awesome-ai-plugins">hashgraph-online/awesome-ai-plugins</a></b> · ⭐691 · Python · 👁️ observed · 0 天</summary>

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
| Stars        | **691**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-assistant` · `ai-plugin` · `awesome` · `awesome-list` · `best-ai-plugins` · `best-antigravity-plugins` · `best-claude-plugins` · `best-codex-plugins`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/morluto/rea">morluto/rea</a></b> · ⭐262085 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **262085** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-05 |

🏷 `agent-skills` · `ai-agents` · `binary-analysis` · `claude-code` · `cli` · `codex` · `cordis` · `decompiler`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/morluto--rea/f46ca8b1518ae39f.png" width="100%" alt="morluto/rea screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/nexu-io/open-design">nexu-io/open-design</a></b> · ⭐101298 · TypeScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create prototypes, websites, apps, dashboards, presentations, images, and videos with your team and AI agents. Share work, exchange feedback, and iterate together in one workspace.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | TypeScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **101298** |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-design` · `byok` · `claude-code-for-design` · `claude-design` · `codex-design` · `coding-agents` · `cursor-design`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/nexu-io--open-design/a1049df34322d3ce.png" width="100%" alt="nexu-io/open-design screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/tt-a1i/archify">tt-a1i/archify</a></b> · ⭐83930 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **83930**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-skills` · `ai-agents` · `architecture-diagram` · `claude-code` · `claude-skills` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/tt-a1i--archify/71b7d4b2427db202.png" width="100%" alt="tt-a1i/archify screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/esengine/DeepSeek-Reasonix">esengine/DeepSeek-Reasonix</a></b> · ⭐35806 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **35806**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-06 |

🏷 `agent` · `agent-framework` · `ai-agent` · `ai-coding` · `cli` · `coding-agent` · `deepseek` · `developer-tools`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/anywhere-labs/dsh-desktop">anywhere-labs/dsh-desktop</a></b> · ⭐30937 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **30937**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `cordis` · `cordis-plugin` · `deepseek` · `deepseek-harness` · `desktop` · `dsh` · `dsh-plugin` · `dsh-plugin-desktop`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/anywhere-labs--dsh-desktop/b72e79b4c3cadb81.png" width="100%" alt="anywhere-labs/dsh-desktop screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/titanwings/distilly">titanwings/distilly</a></b> · ⭐25654 · Python · 🔎 inferred · 2 天</summary>

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
| Stars        | **25654**  |
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
<summary>🧵 <b><a href="https://github.com/awesome-dsh-plugin/awesome-dsh-plugin">awesome-dsh-plugin/awesome-dsh-plugin</a></b> · ⭐18872 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **18872**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `awesome` · `awesome-list` · `deepseek-harness` · `dsh` · `dsh-plugin`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Ebony-Vinyl/dsh-our-free-model">Ebony-Vinyl/dsh-our-free-model</a></b> · ⭐17546 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plugin in dsh: no login, no sign-up, no API key — the frontier models are just there, DeepSeek V4.1 Flash and Kimi K3 among them. Completely free, with no usage cap.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **17546**  |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `ai-agents` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin` · `free-model` · `llm`

</details>

<details>
<summary>🧵 <b><a href="https://github.com/zhu1090093659/dsh-web">zhu1090093659/dsh-web</a></b> · ⭐8790 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **8790**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `dsh-web` · `dsh-web-ui`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/zhu1090093659--dsh-web/5153c3c61827ebb8.jpg" width="100%" alt="zhu1090093659/dsh-web screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/vshulcz/deja-vu">vshulcz/deja-vu</a></b> · ⭐1202 · Go · 🔎 inferred · 0 天</summary>

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
| Stars        | **1202**   |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `agent-memory` · `ai-memory` · `claude-code` · `claude-code-hooks` · `claude-code-plugins` · `codex` · `coding-agents` · `deepseek-harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/8033ba54a9424c88.png" width="100%" alt="vshulcz/deja-vu screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/vshulcz--deja-vu/5fb930f1983f270b.gif" width="100%" alt="vshulcz/deja-vu animation"><br><sub>gravação animada</sub></td>
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
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agent-harness` · `ai-agents` · `cordis` · `decisions-api` · `deepseek-harness` · `dsh` · `dsh-jev` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/luobosibing2--dsh-jev-plugin/e27235473aa310aa.png" width="100%" alt="luobosibing2/dsh-jev-plugin screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Nwflower/dsh-claude-style">Nwflower/dsh-claude-style</a></b> · ⭐164 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **164**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `anthropic` · `claude` · `claude-code` · `claude-desktop` · `cordis` · `dark-mode` · `deepseek-harness` · `desktop-theme`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/screenshots/claude-home-dark.png" width="100%" alt="Nwflower/dsh-claude-style screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Nwflower/dsh-claude-style/master/docs/gifs/idle.gif" width="100%" alt="Nwflower/dsh-claude-style animation"><br><sub>gravação animada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Sutera-Diffusus/dsh-whale-musume">Sutera-Diffusus/dsh-whale-musume</a></b> · ⭐128 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **128**    |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `ai-assistant` · `ai-companion` · `cordis` · `cute` · `deepseek` · `deepseek-harness` · `desktop-app` · `desktop-mascot`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/sutera-diffusus--dsh-whale-musume/cb85aa05cce65f77.png" width="100%" alt="Sutera-Diffusus/dsh-whale-musume screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/BotHarness/DeepSeekBot">BotHarness/DeepSeekBot</a></b> · ⭐96 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **96**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `agent-memory` · `ai-agent` · `bot-marketplace` · `deepseek` · `deepseek-bot` · `deepseek-harness` · `deepseekbot` · `discord-bot`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/1e570820fa589149.jpg" width="100%" alt="BotHarness/DeepSeekBot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/botharness--deepseekbot/bcaac533fb86df37.gif" width="100%" alt="BotHarness/DeepSeekBot animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Fishsb/dsh-prompt-enhancer">Fishsb/dsh-prompt-enhancer</a></b> · ⭐92 · JavaScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **92**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-15 |

🏷 `deepseek` · `deepseek-harness` · `dsh-plugin` · `plugin` · `prompt-engineering`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Fishsb/dsh-prompt-enhancer/main/docs/screenshots/voice-main.png" width="100%" alt="Fishsb/dsh-prompt-enhancer screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/kukucaiCndy/Corum-Harness">kukucaiCndy/Corum-Harness</a></b> · ⭐76 · TypeScript · 🔎 inferred · 0 天</summary>

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
| Stars        | **76**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-11 |

🏷 `agent` · `agent-os` · `ai-agent` · `cordis` · `desktop-app` · `dsh` · `electron` · `harness`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/kukucaicndy--corum-harness/b8971b2831acec9e.png" width="100%" alt="kukucaiCndy/Corum-Harness screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/whyihaveyou/dsh-suite">whyihaveyou/dsh-suite</a></b> · ⭐60 · HTML · 🔎 inferred · 0 天</summary>

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
| Stars        | **60**     |
| Last push    | 2026-10-15 |
| First listed | 2026-10-06 |

🏷 `agent-framework` · `awesome-list` · `cordis` · `deepseek` · `deepseek-harness` · `developer-tools` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/whyihaveyou--dsh-suite/e9daf3bb6313ff1b.png" width="100%" alt="whyihaveyou/dsh-suite screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
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
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `context-window` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `javascript` · `llm` · `model-metadata`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/howillmakeit--dsh-model-context-catalog/3b6ba492f13cdcbf.png" width="100%" alt="HOWILLMAKEIT/dsh-model-context-catalog screenshot"></td>
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
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `agent-security` · `ai-agents` · `ai-security` · `capability-analysis` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/unstone--dsh-xray/35167f8867e8b79d.png" width="100%" alt="unStone/dsh-xray screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/ItQianChen/dsh-github-flow">ItQianChen/dsh-github-flow</a></b> · ⭐5 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

让 DeepSeek Harness Agent 拥有操作 GitHub 的原生手脚！原生复用 gh CLI 安全凭证，支持 PR 自动创建与审查、CI 失败诊断修复、三维待办 Issues、SWR 0ms 秒开全景驾驶舱。

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **5**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-12 |

🏷 `agent-tools` · `ai-agent` · `cordis` · `deepseek-harness` · `developer-tools` · `dsh-plugin` · `gh-cli` · `github-cli`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/itqianchen--dsh-github-flow/e6f0174132cf93c1.png" width="100%" alt="ItQianChen/dsh-github-flow screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/PerryLink/dsh-plugin-doctor">PerryLink/dsh-plugin-doctor</a></b> · ⭐4 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Padrão de verificação sem dependências para plugins do DeepSeek Harness (dsh) — gates de estrutura estática (R), verificações de contrato cordis (K), smoke test em sandbox (D) e verificações de listagem no ecossistema (CC). Padrão de verificação de plugins DSH sem dependências: gates de estrutura estática, verificação de contrato cordis, smoke test em sandbox headless e verificação de inclusão no ecossistema.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **4**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-agent` · `ai-agents` · `cli` · `cordis` · `deepseek-harness` · `developer-tools` · `doctor` · `dsh`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f2d1164a0731d7a5.png" width="100%" alt="PerryLink/dsh-plugin-doctor screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/perrylink--dsh-plugin-doctor/f697a1f89119c87d.gif" width="100%" alt="PerryLink/dsh-plugin-doctor animation"><br><sub>gravação animada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/AI-Scarlett/DSH-Store">AI-Scarlett/DSH-Store</a></b> · ⭐3 · JavaScript · 🔎 inferred · 0 天</summary>

##### 📝 Summary

DSH STORE — marketplace de plugins de terceiros e gerenciador protegido do ciclo de vida para DeepSeek Harness.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | JavaScript                                                                             |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-04 |

🏷 `ai-agents` · `cordis` · `deepseek-harness` · `dsh` · `dsh-plugin` · `plugin-manager` · `plugin-marketplace`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/media/ai-scarlett--dsh-store/b9170b12b3cf26b9.jpg" width="100%" alt="AI-Scarlett/DSH-Store screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

</details>

<details>
<summary>🧵 <b><a href="https://github.com/Atelyx/Atelyx">Atelyx/Atelyx</a></b> · ⭐3 · Rust · 🔎 inferred · 0 天</summary>

##### 📝 Summary

Atelyx é uma bancada de trabalho desktop extensível e centrada nas pessoas: conversas, notas, planilhas e arquivos no mesmo espaço de trabalho; ao criar seu próprio servidor, você ativa colaboração em tempo real entre várias pessoas. O aplicativo em si é um núcleo ultrafino, enquanto funções como conversas, notas, planilhas, canvas, busca e calendário são implementadas por plugins distribuídos com o app, podendo ser desativadas ou substituídas por plugins de terceiros — o objetivo é explorar um novo paradigma de colaboração e trabalho na era da AI.

##### 📌 Basic facts

| Field     | Value                                                                                  |
| --------- | -------------------------------------------------------------------------------------- |
| Category  | `Ecossistemas de plugins do DSH e do Cordis`                                           |
| Evidence  | `declarou um mod, plugin ou hook, mas nada especificamente sobre a superfície de mods` |
| Linguagem | Rust                                                                                   |

##### 📊 Data

| Metric       | Value      |
| ------------ | ---------- |
| Stars        | **3**      |
| Last push    | 2026-10-15 |
| First listed | 2026-10-13 |

🏷 `atelyx-plugin` · `collaboration` · `cordis` · `knowledge-base` · `local-first` · `markdown` · `pkm` · `plugin-platform`

---

<table><tr><th align="center" width="50%">🖼 Imagem</th><th align="center" width="50%">🎬 Vídeo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Atelyx/Atelyx/main/atelyx-app/assets/icons/icon.png" width="100%" alt="Atelyx/Atelyx screenshot"></td>
<td align="center" valign="top"><sub>nenhuma mídia publicada</sub></td>
</tr></table>

<sub>Recurso vinculado diretamente do repositório upstream porque nenhuma licença que permita redistribuição foi declarada.</sub>

</details>

<details>
<summary><b>Mais nesta categoria</b> <sub>· 85</sub></summary>

- [cordiverse/cordis](https://github.com/cordiverse/cordis) - Meta-framework de composabilidade espaço-temporal.
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) - The plugin market inside DeepSeek Harness — browse, search, one-click install ·…
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) - Responda-me com HTML — uma habilidade de agent que responde a perguntas…
- [dsh-tauri/deepseek-harness-desktop](https://github.com/dsh-tauri/deepseek-harness-desktop) - DeepSeek Harness Tauri 桌面版 | Only 8mb installer, zero environment setup, preset…
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) - The best DeepSeek Harness plugin for context insight and management, with…
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Uma proteção pré-execução para agentes de programação com AI.
- [AdamPlatin123/dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar) - DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins…
- [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) - Eyes for text-only DeepSeek Harness agents: built-in free vision chain (no key)…
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) - 📚 Uma biblioteca de microlessons para AI Agents, sem dependências e respaldada…
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) - Cost tracking for DeepSeek Harness: session and model costs, token usage…
- [imsai-sh/awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) - DeepSeek Harness plugin store, marketplace and hub — 11,000+ dsh plugins with…
- [cv-superding/dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login) - Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as…
- [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) - Import conversation history from 25+ AI coding agents into DeepSeek Harness as…
- [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) - Plugin de backup e restauração do DeepSeek Harness (DSH) — exporte, importe…
- [WSL043/dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) - Use your ChatGPT Plus / Pro (Codex) subscription in DeepSeek Harness (DSH)…
- [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) - Mercado de plugins DSH / DSH Plugin Marketplace: navegue, instale e atualize…
- [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) - DeepSeek Harness plugin for previewable cross-preset session migration.
- [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) - Vem instalado com 27 habilidades de engenharia e produtividade de…
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) - 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑.
- [arcships/rutis](https://github.com/arcships/rutis) - Um runtime de plugins para softwares que iteram sobre si mesmos — a base onde…
- [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) - 用于deepseek-harness的opencode-go套餐增强插件。多账号管理、额度UI面板、自动更新模型.
- [SiriLee/dsh-rewind](https://github.com/SiriLee/dsh-rewind) - DSH 插件：便捷无感的同窗口内对话回退，从不新建分支；自带轻量工作区备份，可一并还原文件（Claude Code /rewind 语义）.
- [Microqian2th/dsh-codex-effort-slider](https://github.com/Microqian2th/dsh-codex-effort-slider) - Codex 风格的推理等级滑条（DeepSeek Harness 插件）：可拖动连续滑条 + 高档位渐变星尘特效.
- [WestFox-AwA/dsh-prompt-optimizer](https://github.com/WestFox-AwA/dsh-prompt-optimizer) - DSH 插件 · 注入式优化器 0.8（主线）：你照常说话，它在你发送后,AI接收前把&quot;这一轮到底要什么&quot;理清楚，再把这份理解交给工作 AI(上下文注入)…
- [amlyczz/dsh-agy-link](https://github.com/amlyczz/dsh-agy-link) - Google Antigravity (agy CLI) models for DeepSeek Harness — streaming chat…
- [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) - Diretório selecionado de plugins do DeepSeek Harness (DSH) — mais de 280…
- [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) - DeepSeek Harness MCP Connector: connect servers, search tools across active…
- [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) - dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材.
- [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) - DeepSeek Harness session and workspace manager —— Workspaces: archive and…
- [NekroAI/nekro-nxt](https://github.com/NekroAI/nekro-nxt) - NekroNXT: sistema de agente de chat em grupo multiplataforma baseado no…
- [KannaKuron/dsh-gitbash-shell](https://github.com/KannaKuron/dsh-gitbash-shell) - Plugin do DSH: shell Git Bash para todos os modos de agente em Windows…
- [ali-meoo/meoo-cli](https://github.com/ali-meoo/meoo-cli) - meoo cli 是秒悟（Meoo）官方推出的命令行工具，让 Claude Code、Codex、Cursor、Qoder等本地 agent…
- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) - 给中文网文作者的本地写作工作台.
- [gjj-star/dsh-conversation-navigator](https://github.com/gjj-star/dsh-conversation-navigator) - Navegação de sessões do DSH.
- [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) - Local-first code knowledge graph and context harness for coding agents.
- [awesome-deepseekharness/awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness) - Plugins, ferramentas, habilidades e recursos de aprendizado do DeepSeek Harness…
- [harrylabsj/kiwi](https://github.com/harrylabsj/kiwi) - Runtime de negociação comercial A2A + plugin do DeepSeek Harness (dsh).
- [rezon-aki/dsh-streamfold](https://github.com/rezon-aki/dsh-streamfold) - 流式折叠：会话窗口展示增强——运行时自动展开最新思考小窗、旧过程行折成一条摘要，跑完把思考与工具调用折起而穿插正文保留；逐帧推进，不依赖历史是否加载完.
- [WSL043/dsh-chat-manager](https://github.com/WSL043/dsh-chat-manager) - DeepSeek Harness chat history and session management: search archives, restore…
- [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) - Plugin de memória de projeto em tempo de leitura para o DeepSeek Harness (dsh).
- [pearjelly/deep-blend](https://github.com/pearjelly/deep-blend) - Create and refine Blender product scenes in DSH: editable recipes, model…
- [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) - Continual self-evolution plugin for DeepSeek Harness: versioned, auditable…
- [guzhou079-arch/deepseek-harness-android](https://github.com/guzhou079-arch/deepseek-harness-android) - 把 DeepSeek Harness 打包成能直接装的安卓 APK：不用 Termux、不用 root、不用配环境，21…
- [KCNyu/clawock](https://github.com/KCNyu/clawock) - Stock investment and portfolio decision workflows for AI agents: Claude Code…
- [dshworks/awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) - Registro de plugins, pacotes e habilidades do DeepSeek Harness (dsh), com dados…
- [memorax-ai/dsh-harmony](https://github.com/memorax-ai/dsh-harmony) - A library for patching, replacing and decorating dsh plugin during runtime.
- [tancheng33/dsh-ontology](https://github.com/tancheng33/dsh-ontology) - A typed, inference-capable ontology (TBox + ABox) plugin for DeepSeek Harness…
- [WTStarMark/dsh-plugin-mesh](https://github.com/WTStarMark/dsh-plugin-mesh) - 把带 dsh 系列 GitHub 标签的仓库，画成一张可交互的生态网络图.
- [Ianzhyh/workbuddy-to-dsh](https://github.com/Ianzhyh/workbuddy-to-dsh) - 把本机 WorkBuddy 桌面端已登录的模型（DeepSeek / GLM / Kimi / MiniMax 等）变成本地的 OpenAI 与…
- [memorax-ai/dsh-turn-fold](https://github.com/memorax-ai/dsh-turn-fold) - Codex-style completed-turn folding for DeepSeek Harness, powered by dsh-harmony.
- [earthwalker17/MiniDSH](https://github.com/earthwalker17/MiniDSH) - Minimal surface, complete architecture: a small, local-first coding-agent…
- [poplarity/dsh-science-workbench](https://github.com/poplarity/dsh-science-workbench) - A reproducible science workbench plugin for the DeepSeek Harness: agent-driven…
- [SuperWheel/dsh-cliworker-now](https://github.com/SuperWheel/dsh-cliworker-now) - DeepSeek Harness 多 CLI 智能体侧栏插件：独立对话、账号管理、角色预设与任务续聊.
- [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) - File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a…
- [jiesou/dsh-opencode-zen-free-provider](https://github.com/jiesou/dsh-opencode-zen-free-provider) - OpenCode Zen 免费模型接入 DeepSeek Harness。1M 上下文，同步全部元数据.
- [Max-Null/seek-soul-in-darkness](https://github.com/Max-Null/seek-soul-in-darkness) - Seek Soul in Darkness (SSiD) — DSH-based desktop AI: finding the soul of…
- [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) - Windows desktop pet with DeepSeek billing, Codex subscription quotas, opt-in…
- [stuarthu/dsh-crew](https://github.com/stuarthu/dsh-crew) - dsh plugin: run work as a small crew of role agents.
- [Xizhi1024/deepseek-harness-dsh-for-vscode](https://github.com/Xizhi1024/deepseek-harness-dsh-for-vscode) - DeepSeek Harness(dsh) for VS Code.
- [AKI2253/Sidor_UI](https://github.com/AKI2253/Sidor_UI) - SIDOR starfield skin for DeepSeek Harness Web GUI: intro animation, starfield…
- [reshuibuduo/tmcra-memory](https://github.com/reshuibuduo/tmcra-memory) - TMCRA Core — local-first, scope-isolated long-term memory runtime for AI agents.
- [ywsldxk/dsh-plugin-stars](https://github.com/ywsldxk/dsh-plugin-stars) - DeepSeek Harness (DSH) plugin leaderboard &amp; directory｜DeepSeek…
- [z7ping/agent-lens](https://github.com/z7ping/agent-lens) - Veja claramente cada ação observável dos agentes de codificação de IA.
- [aaronlei/dsh-web-search-diy](https://github.com/aaronlei/dsh-web-search-diy) - DeepSeek Harness（DSH）网页搜索提供方插件：把内置 web_search 工具接到 OpenAI 兼容 Responses API 及其原生…
- [kolawong/fast-compaction-dsh](https://github.com/kolawong/fast-compaction-dsh) - Verdict-based context compaction for DeepSeek Harness — replaces lossy LLM…
- [Kr-ATG/dsh-chat-plus](https://github.com/Kr-ATG/dsh-chat-plus) - DSH 对话体验增强套件（零源码改动，纯插件注入）。Seeker 双栏执行大盘：右栏任务 / 操作面板 / 子智能体 / 产出物四张卡 +…
- [PerryLink/perrylink](https://github.com/PerryLink/perrylink) - Ecossistema de plugins do DeepSeek Harness: 86 plugins de código aberto em uma…
- [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) - DeepSeek Harness plugin market - browse, search &amp; install dsh-plugin topic…
- [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) - Plugin Web do DeepSeek Harness (DSH): aba lateral market-dashboard para…
- [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) - OpenCode no DeepSeek Harness — plugin DSH que mantém OpenCode Zen + modelos de…
- [27painter/dsh-moli](https://github.com/27painter/dsh-moli) - DSH plugin · Drive the local Moli headless browser from DeepSeek Harness…
- [GooDAnDReaDY/dsh-goal](https://github.com/GooDAnDReaDY/dsh-goal) - Autonomous Goal Execution &amp; Multi-Turn Task Tracking Engine with Sticky Header…
- [higekibaka/dsh-vertex-argon](https://github.com/higekibaka/dsh-vertex-argon) - Vertex Argon — Google Vertex AI &amp; Gemini API dual-route Gemini 4 Argon plugin…
- [john-walks-slow/dsh-set-model](https://github.com/john-walks-slow/dsh-set-model) - Through Jev or through its own tool calls, the agent switches model presets and…
- [memorax-ai/dsh-webui-studio](https://github.com/memorax-ai/dsh-webui-studio) - DeepSeek WebUI Studio for interactive, visual-first client plugin development.
- [nailiang002-wq/deepseek-girl-harness](https://github.com/nailiang002-wq/deepseek-girl-harness) - DeepSeek Harness Desktop 互动角色插件：三套服装、任务表情、三口白饭、摸头鼓脸、铁盆帽与手写问候.
- [skkjkk/dsh-usage-dashboard](https://github.com/skkjkk/dsh-usage-dashboard) - DSH (DeepSeek Harness) usage statistics dashboard plugin: token / cost /…
- [viyiviyi/dsh-tree-task-flow](https://github.com/viyiviyi/dsh-tree-task-flow) - 树形任务流 · DeepSeek Harness 插件：把多步任务组织成目标→任务→子任务三级树，节点完成时由 AI…
- [Wanbinyu/wanbinyu-harness-toolbox](https://github.com/Wanbinyu/wanbinyu-harness-toolbox) - Independent third-party plugins and tools for DeepSeek Harness, maintained by…
- [x5427876/dsh-opencode-free](https://github.com/x5427876/dsh-opencode-free) - Use OpenCode Zen free models in DeepSeek Harness with anonymous access or an…
- [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) - DSH 极简风远程移动端，提供「单帧」、「聊天」和「完整」三种模式，将注意力支配权交还给用户.
- [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) - DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成.
- [argszero/cordis-plugin-sandbox-grant-advisor](https://github.com/argszero/cordis-plugin-sandbox-grant-advisor) - Plugin do DeepSeek Harness: transforma a falha de provisionamento da ACL da…
- [zhang-guo-wen/dsh-claude-compat](https://github.com/zhang-guo-wen/dsh-claude-compat) - deepseek harness 插件，兼容claude的skill、rules加载规则，mcp配置.
- [q253595422/dsh-imagegen-video](https://github.com/q253595422/dsh-imagegen-video) - DeepSeek Harness plugin: image + video generation studio with an infinite…

</details>

<a id="writing"></a>

## Textos, discussões e vídeos

Textos, discussões e vídeos sobre a capacidade de mods.

<details>
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50099375">Claude Code Desktop Vulnerability: Preview Pane Data Exfiltration</a></b> · ⭐15 · 👁️ observed · 0 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49945600">Show HN: Terminal Gym – a Claude mod that makes you do pushups between prompts</a></b> · ⭐4 · 👁️ observed · 11 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50003222">What the Hell Are Claude Mods? [video]</a></b> · ⭐4 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49999983">A Claude Code mod plays MIDI music when it works</a></b> · ⭐3 · 👁️ observed · 7 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49925800">Claude Code Mods: plugins may now modify deeper behavior</a></b> · ⭐3 · 👁️ observed · 13 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=50024345">Agent-config&amp;Claude Code mods</a></b> · ⭐2 · 👁️ observed · 5 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49940121">Getting started with Claude Code mods</a></b> · ⭐2 · 👁️ observed · 12 天</summary>

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
<summary>📰 <b><a href="https://news.ycombinator.com/item?id=49934165">Show HN: What&#x27;s Agent Doing – a Claude Code UI mod that explains each step</a></b> · ⭐2 · 👁️ observed · 13 天</summary>

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
| TypeScript | 387      | `anthropics/claude-code`, `anthropics/claude-code-action`, `YeonwooSung/my-claude-code-mods`                  |
| JavaScript | 102      | `karanb192/awesome-claude-code-mods`, `zycck/claude-mods`, `karanb192/claude-code-mods`                       |
| Python     | 38       | `anthropics/claude-agent-sdk-python`, `anthropics/claude-code-security-review`, `alexgreensh/token-optimizer` |
| Shell      | 28       | `anthropics/claude-agent-sdk-typescript`, `0xDarkMatter/claude-mods`, `BeLazy167/claude-mods-skill`           |
| HTML       | 11       | `HeyCubit/effortless`, `darrell-tw/darrelltw-mods`, `omarcevi/claudemods`                                     |
| Rust       | 8        | `helenkwok/rustgis-tui`, `persiyanov/herdr-reviewr`, `ta17eee/claude-code-statusline`                         |
| Go         | 3        | `aaltw/claude-code-statusline`, `esengine/DeepSeek-Reasonix`, `vshulcz/deja-vu`                               |
| PowerShell | 3        | `spyrad/claude-code-statusline`, `ZeyuSi-2099/claude-code-statusline`, `YangShen-SWE/dsh-plugin-simple-pet`   |
| C          | 1        | `reporails/arcade`                                                                                            |
| Java       | 1        | `guzhou079-arch/deepseek-harness-android`                                                                     |
| Swift      | 1        | `necobit/claude-lupin-title`                                                                                  |

<sub>Only entries that declare a language are counted. Documentation and discussion entries are excluded from this table.</sub>

## Contributing

Correções são bem-vindas e são a maneira mais rápida de melhorar esta lista. Abra uma issue ou um pull request se uma entrada estiver na categoria errada, com a classificação errada ou se um projeto tiver sido excluído indevidamente por colisão de nome — essa é a categoria em que filtros automatizados têm maior probabilidade de errar.

---

<sub>Projeto independente da comunidade. Não afiliado, endossado nem revisado por Anthropic. Claude Code, Claude e Anthropic são marcas registradas de Anthropic. O comportamento do produto pode mudar sem aviso; verifique tudo o que for essencial na documentação oficial. Os ativos permanecem propriedade de seus projetos de origem e são reproduzidos somente quando uma licença permite.</sub>

<sub>Last updated · 2026-10-15T23:16:19+08:00</sub>
