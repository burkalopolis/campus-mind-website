# Changelog

## 2026-11-27

- Section system started. Home page rebuilt as coded sections: Hero, Sections 1 to 6. The syllabus form stays a native Grigora form.
- Styles grew from v1 to v1.6 while building Home (cards, icons, image steps, divider, step list, two-column cards, banner, forced centering, flush bottom).
- Learned: Custom HTML blocks don't see site-wide head CSS, so styles travel inside each block. Grigora overrides `<p>` margins.
- Hero link changed from "Watch the 35-second demo" to "See it in a class"; the demo video moves to Faculty Development.
- Check-in length settled at "about 5 minutes" (the demo video says "40 quick statements, about 5 minutes").
- Repo created with styles, sections, build script and paste-ready `dist/` blocks.
- Students page indexed; hero rebuilt with working buttons and a Doing/Being panel (styles v1.7: panel, chips, eight-part colors).
- Students hero live. Section 1 (eight parts in Doing/Being columns with brand colors) ready; styles v1.8.
- Students section 2: heading and check-in iframe combined in one block (id check-in); styles v1.9.
- Students section 3: privacy cards updated for the live check-in, privacy policy link, 988 line.
- Students hero: Doing/Being panel replaced by a wheel of all eight parts with short definitions, introducing the whole-person framework first; styles v1.10.
- Students section 4 (In class): live class check-in, about 5 minutes, share email fixed ("someone you care about"), word cloud alt text, professor link to Join the pilot.
- Eight-parts PDF moved from Google Drive to Grigora Files (root-files/campus-mind-eight-parts.pdf). Students hero and Section 1 link to it. Downloads count in GA4 as file_download (Enhanced measurement; a small onclick sends the event if the block runs in a frame).
- About page indexed and built as five coded sections (styles v1.11: facts row, statement, sources, founder card, avatars, 2×2 cards). USI CDFI bootcamp changed from "current cohort" to completed. Let's talk now leads with Join the pilot.
- Styles v1.12: paragraph spacing forced (Grigora strips it) and a shared text width (`.measure`, 820px) so text, facts and the sources box line up. Applied to About hero, Section 1 and Section 4.
- About Section 3: founder quote changed from blockquote to div (Grigora's blockquote style added italics and an overlapping quote mark); bio runs the full width of the card. Styles v1.13.
- Faculty Development rebuilt as eight coded sections (styles v1.14). Demo video moves near the top; hero leads with Try the demo and Watch the demo; CAP moves lower; tiers and results updated for the live class check-in.
- Faculty Development Section 1 filled with the uploaded demo video and poster, plus a jump-on-load script (Grigora builds the page after the browser's own jump). Home hero link now goes to the Faculty Development demo. Checked live: coded blocks are not in frames, so GA sees clicks directly.
- Brand assets redrawn to match the header (blue C with gold dot; Campus blue, Mind gold, Nunito Bold): `assets/brand/` holds the SVG icon, 32px favicon, 180px app icon, 512px icon and the wordmark PNG for Grigora Settings → Brand assets.
- Media page: five coded sections (styles v1.15: filters, news list, audience tabs, read cards, facts list, contact card). Grigora page /media created through the connection.
