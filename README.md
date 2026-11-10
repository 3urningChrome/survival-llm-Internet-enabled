# Survival LLM

A free AI assistant and survival library that runs entirely on your own computer and works with no
internet. Ask it how to keep food safe in a blackout, treat a burn or purify water: it searches an
offline library of medical, emergency, how-to and encyclopedia articles, answers from what it finds,
and shows you the exact passage each answer came from.

- **Offline and private.** The AI model and the library live on your computer. Your questions never leave it, and once set up it works with the internet off.
- **Shows its sources.** Every answer lists the articles it read; click one to read it yourself, cited passage highlighted, with its license. Ask "where did you get that?" and it opens the source.
- **Shows its reasoning.** Show reasoning, under each answer, opens what the AI thought before it answered, step by step, with the searches and articles it read in between. It stays hidden until you click it.
- **Yours to adjust.** The Instructions button shows the instructions the AI gets before you ask anything (the app adds today's date, the names of your files and your Memory notes after them); edit them any time.
- **Add your own files.** Your files, at the top, takes PDFs, Word documents, EPUB ebooks, web pages and text files (drop them on the window or choose them), so the AI can search your generator's manual, your medicines or other useful files too.
- **Remembers you.** Tell it your daughter is allergic to penicillin or that you have a Honda generator, and it saves a short note so later chats know it too; each answer shows what it saved, with a button to undo it.
- **Updates itself.** Check for updates, at the bottom of the window, looks for a new version (it also looks once a day while it runs, by fetching one small file from the project's web page; nothing about your question is sent there).
- **Built for emergencies.** About 1.5 million articles (500,000 in the smaller download): about 930,000 of Wikipedia's most-read articles, WikiMed, MedlinePlus, a UK medicines guide, WikEM, Ready.gov, AmeriCorp. and more.

## Optional internet search

This project stays offline-first by default. Web search is disabled unless you explicitly enable it:

```bash
export ENABLE_WEB_SEARCH=1
export WEB_SEARCH_PROVIDER=brave
export BRAVE_API_KEY=your_key_here
```

When enabled, the model may use `search_web` for current events or when the offline library does not cover the question. Without a key, Brave search is unavailable; if you prefer a no-key option, use `WEB_SEARCH_PROVIDER=duckduckgo`.

## Install

Do this while you have internet. After that, it needs none. Setup takes 20 minutes to about 2½ hours, depending on
your computer and internet speed (the biggest AI model is 80 GB); you only click for about 5 minutes.

**Mac** (Apple Silicon, macOS 14 Sonoma or newer)
1. Download `Survival-LLM-mac.zip` and double-click it to unzip. Move **Survival LLM** to Applications if you like.
2. Double-click **Survival LLM**. The first time, macOS says it can't verify the app, because it isn't sold through
   Apple. Click **Done**, open **System Settings > Privacy & Security**, scroll down to "Survival LLM was blocked",
   click **Open Anyway**, and confirm with your password. You only do this once.

**Windows** (10 or 11, 64-bit)
1. Download `Survival-LLM-windows.zip`, right-click it and choose **Extract All**. (Running it from inside the zip doesn't work.)
2. Open the extracted **Survival LLM** folder and double-click **Survival LLM.bat**. If Windows says it protected
   your PC, click **More info**, then **Run anyway**.

**Then** the app opens in its own window and walks you through setup:
1. **AI engine:** built into the Mac app. On Windows, one click downloads it (Ollama, 1.6 GB).
2. **AI model:** it suggests the best one for your computer's memory (below) and downloads it.
3. **Library:** "Everything" (8.8 GB download) or "Essentials" (1.3 GB, without Wikipedia and iFixit).

**Free disk space needed:** the model's size plus 5 GB, plus about 27 GB while the full library installs
(21 GB once installed), or about 10 GB for Essentials (3 GB once installed).

## License

Code: MIT ([LICENSE](LICENSE)). Library content keeps the license of its source ([SOURCES.md](SOURCES.md)).

AI models make mistakes. Every answer shows its sources so you can check.
