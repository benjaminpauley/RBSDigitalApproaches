## Zotero translators 
### English Short Title Catalogue
Out of the box, Zotero will ingest records from the English Short Title Catalogue quite happily, using the translator for Aleph library catalogues in conjunction with the MARC translator. The default behavior isn't especially well-suited for working with ESTC records, however. These translators make a few tweaks to improve things.

There are *two* javascript files here, which both need to be added to Zotero's collection of translators. `English Short Title Catalogue.js` notes when you're at the ESTC and directs Zotero to use the second file, `MARC-2.js` in place of the standard `MARC.js` translator. `MARC-2 .js`is just a slightly altered version of the standard `MARC.js` translator that:
* Grabs the ESTC citation number and places it in the "Extra" field.
* Grabs the entire, messy pagination statement (rather than just the first thing that looks like a number).
* Inclues citation notes (the MARC 510 field) in Zotero notes
* Separates multiple notes with a pipe character (`' | '`) for easier parsing later.

### Short-Title Catalogue, Netherlands
Like the ESTC translators, this translator makes a few tweaks to the existing PICA translator to make the results that Zotero imports more friendly for book historical work:
* The STCN fingerprint goes in the "Extra" field.
* The imprint information gets split into city and publisher fields.
* The format and collation statement gets put into the number of pages field.
* Typographical information gets saved as a note.

These translators lean very, very heavily on the work of the original developers, Simon Kornblith, Sylvain Machefert, Michael Berkowitz, Ming Yeung Cheung, and Sebastian Karcher. Duplicating the work of the `MARC.js` module for the ESTC translator strikes me as a particularly inelegant kludge, but I take some comfort in seeing that that seems to be more or less the same approach that was used to adapt the Aleph translator to deal with quirks of one library's OPAC using the `MAB2.js` translator.

If you're using Mac OS X, these javascript files need to go in the folder located	 at `/Users/<your-username>/Library/Application Support/Zotero/Profiles/<your-profile>.default/zotero/translators`. (You can navigate to this folder in the Finder by holding down the `option` key while selecting the `Go` menu, which will reveal the ordinarily-hidden `Library` folder. If you are using Windows, you'll first need to set Windows Explorer to view hidden files. If you are using Zotero Firefox, add the files to `C://Users/<your-username>/AppData/Roaming/Mozilla/Profiles/<your-profile>.default/zotero/translators`. If you are using Zotero Standalone, add them to `C://Users/<your-username>/AppData/Roaming/Zotero/Profiles/<your-profile>.default/zotero/translators`.)
  
I've tested these translators on Mac OS X only. They work work with Zotero Firefox and with Zotero Standalone when using Safari and Chrome. For quite some time I thought there was something keeping the translator from working with Safari, but the problem went away when I disabled all other Safari extensions and then re-enabled them. (If there was interference between two extensions, it seems to have resolved itself after a disable/enable cycle.)