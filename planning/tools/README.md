# Wiki dump tools

`haikyuufandomcom-20200223-history.xml.7z` (repo root) is the full Haikyuu fandom wiki history, Feb 23 2020, from the Internet Archive.

To use it in a new session:

```bash
pip install py7zr
python3 -I -c "import py7zr,sys; py7zr.SevenZipFile(sys.argv[1]).extractall(sys.argv[2])" haikyuufandomcom-20200223-history.xml.7z <scratch>/wiki
python3 -I planning/tools/split_wiki.py <scratch>/wiki/haikyuufandomcom-20200223-history.xml <scratch>/wikipages
```

`split_wiki.py` writes the newest revision of every article and category page as `<Title>.txt` (non-alphanumerics become `_`). Build a chapter index with:

```bash
cd <scratch>/wikipages && for f in *.txt; do n=$(grep -m1 -oP '^\|\s*chapter number\s*=\s*\K[0-9]+' "$f"); [ -n "$n" ] && echo "$n	$f"; done | sort -n > ../chapter_index.tsv
```
