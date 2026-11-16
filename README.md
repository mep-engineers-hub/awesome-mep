# awesome-mep

> **Unverified. Not for stamped or issued work. Check against the adopted code edition.**

An annotated index of software tools for mechanical, electrical and plumbing (MEP) design, **tested by practicing engineers**. Each entry says who tried it, how, and against which worked example.

This is not a broad AEC directory. For that, see [Awesome AECO](https://github.com/osama-ata/Awesome-AECO), the [OSC Directory](https://opensource.construction/projects/), [OSArch](https://osarch.org/) and the [OSArch AEC Free Software directory](https://wiki.osarch.org/aec-free-software-directory/).

## Tiers

| Tier | Meaning |
| --- | --- |
| Found | Listed from public information. Nobody here has run it yet. |
| Tried | A member installed and ran it on a realistic case and recorded the result. |
| Validated against a worked example | A member reproduced a published worked example and linked the comparison. |

"Validated" means one worked example was reproduced. It **never** means code-compliant, certified or approved for design. See [TIERS.md](TIERS.md).

License flags: ⚠ copyleft: GPL, AGPL, LGPL or MPL (the cell names which; check before commercial use) · 🔒 custom, source-available or non-OSI license (read the terms before any reuse) · ⛔ no license (do not reuse code) · ❔ NOASSERTION or non-standard license text (open the LICENSE file before reuse).

Seed entries (15.11.2026 and 16.11.2026) are tier Found: listed from public information, licenses read from each repo on those dates. Nobody here has run them yet. Platform is the host app or the repo's main language as GitHub reports it.

## Contents

- [HVAC loads and psychrometrics](#hvac-loads-and-psychrometrics)
- [Duct and pipe sizing](#duct-and-pipe-sizing)
- [Pumps and fans](#pumps-and-fans)
- [Plumbing and drainage](#plumbing-and-drainage)
- [Fire protection](#fire-protection)
- [Electrical (links only)](#electrical-links-only)
- [Multi-discipline suites](#multi-discipline-suites)
- [Equipment data](#equipment-data)
- [CAD/BIM data exchange](#cadbim-data-exchange)
- [Python libraries](#python-libraries)
- [AI agents and automation](#ai-agents-and-automation)
- [UAE/GCC workflow notes](#uaegcc-workflow-notes)
- [Related lists](#related-lists)

Each section uses the same table. Full details of each entry (worked example, limits) go in [`entries/`](entries/), one file per tool, based on [ENTRY_TEMPLATE.md](ENTRY_TEMPLATE.md).

## HVAC loads and psychrometrics

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [psychrometrics/psychrolib](https://github.com/psychrometrics/psychrolib) | Psychrometric property functions (ASHRAE psychrometric equations; edition per repo docs). | MIT | Library (multi-language) | Tried | HusseinRagab / 15.11.2026 | [psychrolib](entries/psychrolib.md) |
| [CoolProp/CoolProp](https://github.com/CoolProp/CoolProp) | Fluid, refrigerant and humid-air property library. | MIT | Library (C++, wrappers) | Found | — | — |
| [portyanikhin/pyfluids](https://github.com/portyanikhin/pyfluids) | Python wrapper over CoolProp. | MIT | Python library | Tried | HusseinRagab / 15.11.2026 | [pyfluids](entries/pyfluids.md) |
| [TomLXXVI/python-hvac](https://github.com/TomLXXVI/python-hvac) | HVAC loads (RTS method) plus air, hydronic and refrigeration helpers. | MIT | Python library | Tried | HusseinRagab / 15.11.2026 | [python-hvac](entries/python-hvac.md) |
| [simeononsecurity/Manual-J-Load-Calculator](https://github.com/simeononsecurity/Manual-J-Load-Calculator) | Residential load calculator (Manual J method). | MIT | Web (JavaScript) | Found | — | — |
| [azogue/psychrochart](https://github.com/azogue/psychrochart) | Draws psychrometric charts with overlays of points, lines and zones. | MIT | Python library | Found | — | — |
| [pythermalcomfort/pythermalcomfort](https://github.com/pythermalcomfort/pythermalcomfort) | Thermal comfort indices, including PMV/PPD and adaptive models. | MIT | Python library | Found | — | — |
| [LBNL-ETA/EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | MCP server that lets an AI agent set up and run EnergyPlus models; exploratory. | ❔ BSD-style (LBNL License.txt) | MCP server (Python) | Found | — | — |

## Duct and pipe sizing

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [CalebBell/fluids](https://github.com/CalebBell/fluids) | Pipe friction, fittings, pumps and pipe schedules. | MIT | Python library | Tried | HusseinRagab / 15.11.2026 | [fluids](entries/fluids.md) |
| [USEPA/WNTR](https://github.com/USEPA/WNTR) | EPANET-compatible water network solver. | ❔ NOASSERTION | Python library | Found | — | — |
| [akseidel/WpfaksDuctOMatic](https://github.com/akseidel/WpfaksDuctOMatic) | Duct calculator; inactive since 2021. | MIT | Windows (WPF, C#) | Found | — | — |
| [ashpursglove/Ashs_MEP_Playground](https://github.com/ashpursglove/Ashs_MEP_Playground) | Piping hydraulics diagrams and electrical single-line drawings. | ⛔ none | Web (TypeScript) | Found | — | — |
| [e2nIEE/pandapipes](https://github.com/e2nIEE/pandapipes) | Steady-state solver for looped pipe networks (water, gas, heat). | BSD-3-Clause | Python library | Found | — | — |
| [wangzhichao-jpg/OpenHydroNet](https://github.com/wangzhichao-jpg/OpenHydroNet) | Hydronic balancing with index-circuit and scenario runs; ships validation and known-limits notes. New repo. | Apache-2.0 | Python/Electron | Found | — | — |
| [jlillywh/RTHYM-MOC](https://github.com/jlillywh/RTHYM-MOC) | Water-hammer transient analysis by the method of characteristics. Small, new repo. | MIT | Python | Found | — | — |

## Pumps and fans

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [jmoro0408/Pump-Plotting](https://github.com/jmoro0408/Pump-Plotting) | Plots a pump curve to PDF from Excel data. | ⛔ none | Python script | Found | — | — |

## Plumbing and drainage

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [seanturner82/plumbing-fixtture-calculator](https://github.com/seanturner82/plumbing-fixtture-calculator) | Fixture-unit calculator (IPC method; edition not stated). | ⛔ none | Web (TypeScript) | Found | — | — |

## Fire protection

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [DonVito1982/SprayHydraulic](https://github.com/DonVito1982/SprayHydraulic) | Hazen-Williams sprinkler network solver. | ⛔ none | Python | Found | — | — |
| [yeoyong2002-coder/K-Fire-Hydraulic-Solver](https://github.com/yeoyong2002-coder/K-Fire-Hydraulic-Solver) | Sprinkler hydraulics solver (Korean). | ⛔ none | Not stated | Found | — | — |
| [eliteweblabs/fire-pump-curve-app](https://github.com/eliteweblabs/fire-pump-curve-app) | Fire-pump curve from three rated points. | ⛔ none | Web (JavaScript) | Found | — | — |
| [jmdreher1-svg/Fire-Pump-Test-Curves](https://github.com/jmdreher1-svg/Fire-Pump-Test-Curves) | Fire-pump test curve plotter (Chart.js). | ⛔ none | Web (HTML) | Found | — | — |
| [FireDynamics/fdsreader](https://github.com/FireDynamics/fdsreader) | Reads FDS fire-simulation output for post-processing. | ⚠ GPL-3.0 | Python library | Found | — | — |

## Electrical (links only)

Listed for completeness; not tested by this group.

| Tool | What it does | License | Platform | Link |
| --- | --- | --- | --- | --- |
| [haydenburrows30/qmlElectrical](https://github.com/haydenburrows30/qmlElectrical) | Cable sizing and voltage-drop calculator. | MIT | Desktop (Python, QML) | [GitHub](https://github.com/haydenburrows30/qmlElectrical) |
| [e2nIEE/pandapower](https://github.com/e2nIEE/pandapower) | Power-system load flow and short-circuit analysis. | BSD-3-Clause | Python library | [GitHub](https://github.com/e2nIEE/pandapower) |

## Multi-discipline suites

Tools that cover several MEP disciplines in one package.

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [kakarot-oncloud/openmep-suite](https://github.com/kakarot-oncloud/openmep-suite) | Web suite for HVAC, plumbing, electrical and fire; cites BS, IEC and ASHRAE methods. | MIT | Web (Python) | Found | — | — |
| [novatechhvac/MEPQuickCalc](https://github.com/novatechhvac/MEPQuickCalc) | Offline page that claims many MEP calculators; claims not checked. | ⛔ none | Web (HTML, offline) | Found | — | — |

## Equipment data

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [wangzhichao-jpg/fintube-hx](https://github.com/wangzhichao-jpg/fintube-hx) | Fin-and-tube coil rating with a published measured-data comparison and stated tolerances. Open-core: a paid tier exists. | MIT | Python library | Found | — | — |
| [wangzhichao-jpg/opencompressor-twin](https://github.com/wangzhichao-jpg/opencompressor-twin) | Compressor performance model with a stated validity range on fitted curves; research preview. | MIT | Python library | Found | — | — |

## CAD/BIM data exchange

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [mozman/ezdxf](https://github.com/mozman/ezdxf) | Read and write DXF files. | MIT | Python library | Tried | HusseinRagab / 15.11.2026 | [ezdxf](entries/ezdxf.md) |
| [stevenkfirth/xgbxml](https://github.com/stevenkfirth/xgbxml) | Create and edit gbXML. | MIT | Python library | Found | — | — |
| [storytold/cadcraft](https://github.com/storytold/cadcraft) | Clean-room 2D/3D CAD for DXF and DWG, with CLI and MCP access. | Apache-2.0 | Desktop/CLI (Rust) | Found | — | — |
| [lookup-foundation/RevitLookup](https://github.com/lookup-foundation/RevitLookup) | Revit API explorer for elements and parameters. | MIT | Revit add-in (C#) | Found | — | — |
| [Nice3point/RevitTemplates](https://github.com/Nice3point/RevitTemplates) | Templates for new Revit add-in projects. | MIT | Revit add-in templates (C#) | Found | — | — |
| [bimone/addins-excelexporterimporter](https://github.com/bimone/addins-excelexporterimporter) | Revit schedule export to and import from Excel. | MIT | Revit add-in (C#) | Found | — | — |
| [kristiangl/RevitSheetExporter](https://github.com/kristiangl/RevitSheetExporter) | Bulk export of Revit sheets to PDF, DWG and IFC. | MIT | Revit add-in (C#) | Found | — | — |
| [M2Dawn/BIM-Automation-Tool](https://github.com/M2Dawn/BIM-Automation-Tool) | Batch export of DWG, PDF, IFC, NWC and schedules. | MIT | Revit add-in (C#) | Found | — | — |
| [Cazorlas/PaperPlus](https://github.com/Cazorlas/PaperPlus) | Revit add-in with batch PDF and DWG export among other tools. | BSL-1.0 | Revit add-in | Found | — | — |
| [pyrevitlabs/pyRevit](https://github.com/pyrevitlabs/pyRevit) | Python platform for building Revit tools. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [ErikFrits/EF-Tools](https://github.com/ErikFrits/EF-Tools) | pyRevit tools for sheets, renumbering, renaming and selection. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [Seed-43/Seed43](https://github.com/Seed-43/Seed43) | pyRevit productivity suite. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [datadrivenconstruction/ImportExcelToRevit](https://github.com/datadrivenconstruction/ImportExcelToRevit) | Imports parameter values into Revit from Excel. | ⚠ GPL-3.0 | Revit (Dynamo/script) | Found | — | — |
| [gtalarico/pyrevitplus](https://github.com/gtalarico/pyrevitplus) | pyRevit+ helpers, including open-in-Excel; stale. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [tillbaum/pytiba](https://github.com/tillbaum/pytiba) | pyRevit PDF export tool. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [permpong13/P13](https://github.com/permpong13/P13) | pyRevit helpers for Excel schedules, sheets, parameters and MEP. | ⛔ none | Revit (pyRevit) | Found | — | — |
| [DomCR/ACadSharp](https://github.com/DomCR/ACadSharp) | Reads and writes DWG (AC1014 to AC1032) and DXF. | MIT | .NET library (C#) | Found | — | — |
| [monozukuri-ai/ezdwg](https://github.com/monozukuri-ai/ezdwg) | Reads DWG files from Python. Small, new repo. | MIT | Python library (Rust core) | Found | — | — |
| [aegis1980/cad-to-shapely](https://github.com/aegis1980/cad-to-shapely) | Turns DXF geometry into shapely polygons, for example room outlines. | MIT | Python library | Found | — | — |
| [mlightcad/cad-viewer](https://github.com/mlightcad/cad-viewer) | Views DWG and DXF drawings in a web browser. | MIT | Web (TypeScript) | Found | — | — |
| [CEXT-Dan/PyRx](https://github.com/CEXT-Dan/PyRx) | Runs Python inside AutoCAD and compatible CAD hosts. | ⚠ LGPL-3.0 | AutoCAD plug-in (C++) | Found | — | — |
| [BIM2SIM/bim2sim](https://github.com/BIM2SIM/bim2sim) | Converts IFC models into thermal zones and building-simulation inputs. | ⚠ LGPL-3.0 | Python library | Found | — | — |
| [chuongmep/OpenMEP](https://github.com/chuongmep/OpenMEP) | Dynamo nodes for MEP elements in Revit. | MIT | Revit (Dynamo, C#) | Found | — | — |
| [bvn-architecture/RevitBatchProcessor](https://github.com/bvn-architecture/RevitBatchProcessor) | Runs scripted tasks on many Revit files in batch. | ⚠ GPL-3.0 | Revit (Python) | Found | — | — |
| [CyrilWaechter/pyRevitMEP](https://github.com/CyrilWaechter/pyRevitMEP) | pyRevit tools aimed at MEP modelling. | ⚠ GPL-3.0 | Revit (pyRevit) | Found | — | — |
| [PerkinsAndWill-IO/sPrint](https://github.com/PerkinsAndWill-IO/sPrint) | Browser extension for batch printing sheets from Autodesk Construction Cloud. | MIT | Chrome extension (TypeScript) | Found | — | — |
| [DynMEP/YOLOplan](https://github.com/DynMEP/YOLOplan) | Detects and counts symbols on drawings with a YOLO model. | ⚠ AGPL-3.0 | Python | Found | — | — |
| [permitzip/mutinybim](https://github.com/permitzip/mutinybim) | Browser-based BIM engine with trade add-ons. | Apache-2.0 | Web (TypeScript) | Found | — | — |
| [OpenAEC-Foundation/ifccad](https://github.com/OpenAEC-Foundation/ifccad) | Drawing profile for IFC5/IFCX; alpha. | ⚠ MPL-2.0 | Rust | Found | — | — |

## Python libraries

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [CalebBell/ht](https://github.com/CalebBell/ht) | Heat-transfer library, sister to fluids. | MIT | Python library | Found | — | — |
| [hgrecco/pint](https://github.com/hgrecco/pint) | Units library for SI and inch-pound quantities. | ❔ NOASSERTION | Python library | Found | — | — |
| [CalebBell/thermo](https://github.com/CalebBell/thermo) | Thermodynamic properties of chemicals and mixtures, sister to fluids and ht. | MIT | Python library | Found | — | — |

## AI agents and automation

### CAD and BIM agents

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [autodesk-platform-services/aps-sample-mcp-server-revit-automation](https://github.com/autodesk-platform-services/aps-sample-mcp-server-revit-automation) | Autodesk sample MCP server for cloud Revit Automation. | MIT | MCP server (C#) | Found | — | — |
| [mcp-servers-for-revit/mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit) | Community Revit MCP server for rooms, pipes and elements. | MIT | MCP server (C#) | Found | — | — |
| [mcp-servers-for-revit/mcp-server-for-revit-python](https://github.com/mcp-servers-for-revit/mcp-server-for-revit-python) | pyRevit-based Revit MCP server; work in progress. | MIT | MCP server (Python) | Found | — | — |
| [General-Soju/BimOnMcp](https://github.com/General-Soju/BimOnMcp) | MCP bridge for Revit and AutoCAD (IronPython, Dynamo). | ❔ NOASSERTION | MCP server (C#) | Found | — | — |
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | AutoCAD LT MCP server that dispatches commands through AutoLISP. | MIT | MCP server (Python) | Found | — | — |
| [U-C4N/Autocad-MCP](https://github.com/U-C4N/Autocad-MCP) | AutoCAD MCP via COM, plus headless DXF work with ezdxf. | MIT | MCP server (Python) | Found | — | — |
| [shtirlitsDva/cad-mcp](https://github.com/shtirlitsDva/cad-mcp) | In-process MCP for AutoCAD and Revit. | ⛔ none | MCP server (C#) | Found | — | — |
| [bimwright/rvt-mcp](https://github.com/bimwright/rvt-mcp) | Local MCP server for Revit with a large tool set; README lists Revit 2022 to 2027. | Apache-2.0 | MCP server (C#) | Found | — | — |
| [bimwright/dwg-mcp](https://github.com/bimwright/dwg-mcp) | AutoCAD MCP server that confirms the target drawing before it writes. | Apache-2.0 | MCP server (C#) | Found | — | — |
| [id0o0bi/autocad-mcp](https://github.com/id0o0bi/autocad-mcp) | Agent edits of DXF/DWG through ezdxf first. Small, new repo. | MIT | MCP server (Python) | Found | — | — |
| [QuanZ827/zexus](https://github.com/QuanZ827/zexus) | Revit agent that shows a plan and waits for user confirmation before changing the model; README lists Revit 2022 to 2026. | Apache-2.0 | Revit add-in (C#) | Found | — | — |
| [hamzaabduljabbar/autoconst-spec-compliance-claude](https://github.com/hamzaabduljabbar/autoconst-spec-compliance-claude) | Checks Revit elements against clauses pulled from a project specification and reports pass or fail. Code is not reusable under its license. | 🔒 custom (source-available) | Python | Found | — | — |
| [ADN-DevTech/acad-api-skill](https://github.com/ADN-DevTech/acad-api-skill) | Agent skill from Autodesk developer support for writing AutoCAD .NET plug-ins. | MIT | Agent skill (PowerShell) | Found | — | — |

### General agent and developer tools

Not MEP-specific. Listed because members use them to build and check their own tools. Same tiers and license flags apply.

#### Agent skills and plugins

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. | MIT | JavaScript | Found | — | — |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | An agent harness covering skills, instincts, memory, security and research-first development. | MIT | JavaScript | Found | — | — |
| [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Official, Anthropic-managed directory of Claude Code plugins. | Apache-2.0 | Python | Found | — | — |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Open plugins aimed at knowledge work in Claude Cowork. | Apache-2.0 | Python | Found | — | — |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's public agent skills, including document skills for docx, pdf, pptx and xlsx. | ⛔ none | Python | Found | — | — |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with machine-readable findings. | MIT | JavaScript | Found | — | — |
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor plugin specification and official plugins. | ⛔ none | TypeScript | Found | — | — |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Claude Code skill pack with Think, Plan, Build and Ship roles. | MIT | TypeScript | Found | — | — |
| [github/spec-kit](https://github.com/github/spec-kit) | Playbooks that take a written spec through build and bugfix work with coding agents. | MIT | Python | Found | — | — |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | A large library of scientific skills for AI agents. | MIT | Python | Found | — | — |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Engineering-focused agent skills taken from the author's own agents directory. | MIT | Shell | Found | — | — |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | A free local plugin that keeps bulky tool output out of a coding agent's context window. | ❔ NOASSERTION | JavaScript | Found | — | — |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | A large set of role-based agent skills, from frontend work to research. | MIT | Shell | Found | — | — |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | A single `CLAUDE.md` file derived from Andrej Karpathy's notes on LLM coding pitfalls. | ⛔ none | Not stated | Found | — | — |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Security scanner for agent and MCP skills, with a library of known patterns. | Apache-2.0 | Python | Found | — | — |
| [obra/superpowers](https://github.com/obra/superpowers) | An agentic skills framework and software-development methodology. | MIT | Shell | Found | — | — |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | The open agent-skills CLI and catalog, including the find-skills meta-skill. | MIT | TypeScript | Found | — | — |

#### MCP servers and agent frameworks

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Long-term memory and handoff between different coding-agent vendors. | MIT | Rust | Found | — | — |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | An AI gateway that calls many LLM APIs in one format, with cost tracking. | ❔ NOASSERTION | Python | Found | — | — |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Turns a codebase, its docs, schemas and PDFs into a queryable knowledge graph. | Apache-2.0 | Python | Found | — | — |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Compresses tool outputs, logs, files and RAG chunks before they reach the model. | Apache-2.0 | Python | Found | — | — |
| [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Wraps software so agents can drive it through CLIs. | Apache-2.0 | Python | Found | — | — |
| [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Local desktop chat app that runs agents through Grok and Claude CLIs. | Apache-2.0 | TypeScript | Found | — | — |
| [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | An ontology layer over data, exposed as MCP, CLI and API. | Apache-2.0 | Python | Found | — | — |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | A multi-agent harness for swarms and coordinated workflows. | MIT | TypeScript | Found | — | — |
| [stablyai/orca](https://github.com/stablyai/orca) | Runs a fleet of coding agents from your own subscription, on desktop, mobile or remote. | MIT | TypeScript | Found | — | — |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Persistent memory that captures, compresses and re-injects agent session context. | Apache-2.0 | TypeScript | Found | — | — |
| [trycua/cua](https://github.com/trycua/cua) | Open-source computer-use drivers, cross-OS sandboxes and benchmarks. | MIT | Rust | Found | — | — |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | An agent-memory system designed to learn over time. | MIT | Python | Found | — | — |
| [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Browser automation CLI and MCP server for agents. | Apache-2.0 | Rust | Found | — | — |
| [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Lets agents operate desktop apps through the accessibility tree. | Apache-2.0 | Rust | Found | — | — |
| [xerj-org/xerj](https://github.com/xerj-org/xerj) | AI search engine and MCP server that indexes code, docs, logs and PDFs. | Apache-2.0 | Rust | Found | — | — |

#### Coding agents and dev workflow

| Tool | What it does | License | Platform | Tier | Tested by / date | Details |
| --- | --- | --- | --- | --- | --- | --- |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | A hybrid deterministic-plus-LLM code-review tool. | Apache-2.0 | Go | Found | — | — |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | A fast Python linter and formatter, written in Rust. | MIT | Rust | Found | — | — |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | A local browser workspace to mark up agents' plans, specs, HTML and code diffs, then send comments back. | Apache-2.0 | TypeScript | Found | — | — |
| [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os) | An agent workspace built on Cloudflare Workers for documents, apps and company context. | Apache-2.0 | TypeScript | Found | — | — |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | Self-hostable AI coworkers that each get a browser, files and tools, and wait for approval before acting. | MIT | TypeScript | Found | — | — |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | A skill that pushes coding agents to write less code and avoid unnecessary work. | MIT | JavaScript | Found | — | — |
| [e2e-inc/e2e](https://github.com/e2e-inc/e2e) | An end-to-end testing framework for web and mobile apps. | Apache-2.0 | TypeScript | Found | — | — |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | Independent auditing of AI agents, run by a human or by the agent itself. | Apache-2.0 | Python | Found | — | — |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | A skill and proxy that shortens agent prompts into terse language to cut tokens. | Apache-2.0 | Go | Found | — | — |
| [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | A Git worktree CLI for running several local agents in parallel. | Apache-2.0 | Rust | Found | — | — |
| [morluto/rea](https://github.com/morluto/rea) | An agent toolkit for reverse-engineering app behavior down to native binaries. | MIT | TypeScript | Found | — | — |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | A safe, private runtime for autonomous AI agents. | Apache-2.0 | Rust | Found | — | — |
| [openai/codex-security](https://github.com/openai/codex-security) | CLI and SDK that finds, validates and drafts fixes for security vulnerabilities, with SARIF and other exports. | Apache-2.0 | TypeScript | Found | — | — |
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | A way to control Claude Code, Codex and similar tools from any computer or phone. | MIT | TypeScript | Found | — | — |
| [shadcn/improve](https://github.com/shadcn/improve) | An agent skill that audits a codebase and writes self-contained markdown plans, but never implements them. | MIT | Not stated | Found | — | — |
| [Tencent/LoopForge](https://github.com/Tencent/LoopForge) | Self-hosted workspace that runs coding-agent CLIs in sandboxes, with repeatable SOPs and human approval gates. | ❔ NOASSERTION | Go | Found | — | — |
| [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) | An AI pull-request reviewer that runs as a GitHub Action. | MIT | Python | Found | — | — |

## UAE/GCC workflow notes

Short notes on local authority workflows. Citations only (document, edition, clause #); no code text.

No notes yet. Suggest one by pull request or in [Discussions](../../discussions).

## Related lists

Other curated lists. Not tools, so no tier.

| List | What it covers | License |
| --- | --- | --- |
| [ishandutta2007/Awesome-HVAC-Operational-Efficiency-Optimization](https://github.com/ishandutta2007/Awesome-HVAC-Operational-Efficiency-Optimization) | HVAC operations, controls and BACnet resources. | MIT |
| [mitevpi/awesome-bim](https://github.com/mitevpi/awesome-bim) | BIM, Revit, Python and C# resources; stale since 2019. | MIT |
| [opensource-construction/osc-directory](https://github.com/opensource-construction/osc-directory) | Source of the OSC Directory of open-source AEC tools. | MIT |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Questions go to [Discussions](../../discussions).

## License

The index and docs are licensed [CC BY 4.0](LICENSE). Listed tools keep their own licenses.
