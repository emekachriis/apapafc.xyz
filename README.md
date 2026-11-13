# apapakingsfc.xyz

Website for **Apapa Kings FC** (Lagos, Nigeria · Est. 2025 · *Kings Never Settle*).

It is a static site built by **GitHub Pages** (Jekyll) automatically every time you push.
There is nothing to install: edit a file, commit, push, and the site updates in a minute or two.

## Where things live

| You want to change… | Edit this file |
| --- | --- |
| Email, WhatsApp, TikTok, season year | `_data/club.yml` |
| Players & coaches | `_data/squad.yml` |
| Fixtures & results | `_data/fixtures.yml` |
| News / match reports | one file per article in `_posts/` |
| Menu links | `_data/nav.yml` |
| Page wording | `index.html`, `about.html`, `join.html`, … |
| Colours & fonts | top of `assets/css/main.css` (`:root`) |

The season record (played, won, goals, form guide), the home-page "Next match" and
"Last result", and the match-report links all work themselves out from these files.

## Common jobs

### Add an upcoming match
Add a block to the bottom of `_data/fixtures.yml` **without** a `score`:

```yaml
- date: 2026-12-06
  kickoff: "16:00"
  opponent: Somebody FC
  home: true
  venue: Isolo Pitch
```

The first match without a score becomes the **Next match** (with a live countdown) on the
home and fixtures pages. With no upcoming match, the site shows a "Date TBC / Your team?" panel
inviting teams to arrange a friendly.

### Record the result
Add the score to that same block. **Kings' goals first**, whatever the venue:

```yaml
  score: "2-1"   # Kings scored 2, they scored 1
```

### Write a match report
Create a file in `_posts/` named `YYYY-MM-DD-short-title.md`:

```markdown
---
title: "Kings beat Somebody FC 2–1"
kind: match-report          # or club-news
match: "2026-12-06"         # same date as the fixture → shows the scoreline + links from Fixtures
image: /images/photos/match9.jpg   # optional
---
Write the report here. Blank line between paragraphs. **bold**, [links](/squad/).
```

### Add a player or a photo
Add a block to `_data/squad.yml`. For a photo, run (needs Python with Pillow):

```bash
python3 tools/optimise_photos.py player images/NEWGUY.jpg
```

That saves a small, phone-friendly copy to `images/players/newguy.jpg`. Then add
`photo: images/players/newguy.jpg` to the player. No photo? The player gets a printed-shirt
placeholder with their name and number.

Match photos: `python3 tools/optimise_photos.py photo images/match9.jpg` → `images/photos/`.

## Preview on your own computer (optional)

```bash
gem install jekyll -v 3.10.0 && gem install jekyll-redirect-from jekyll-sitemap kramdown-parser-gfm webrick
```

```bash
jekyll serve
```

Then open http://localhost:4000.

## Notes
- Old addresses (`squad.html`, `fixtures.html`, `news.html`) redirect to the new pages;
  `gallery.html` goes to the home page and `sponsors.html` to Join & Contact.
- Original full-size photos stay in `images/`; the site uses the optimised copies in
  `images/players/` and `images/photos/`.
- The "Send on WhatsApp" forms on the Join page don't need a server: they open WhatsApp
  with the message already typed.
