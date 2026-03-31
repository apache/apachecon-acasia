# ApacheCon hugo site

This repository contains a Hugo based site for ApacheCon.

NOTE: Please use **hugo v0.92.2** to avoid the website build error.

To install Hugo :

```
brew install hugo
# or
port install hugo
```

Please chose hugo below v0.93, otherwise the build will failed.  

To test it locally, run:

```
hugo server -b http://localhost:1313/acasia2023 -F
```

To generate final site, use:


```
hugo -b https://apachecon.com/acasia2023/ -d <destination_directory> -F
```

## FAQ

### How to fix the typos in Session page
If you want to fix session typos of https://asia.communityovercode.org/sessions/cloudnative-913295.html
You just need to go the file cloudnative-913295.md in content/sessions directory.
If it is chinese version, you just need to update the file of cloudnative-913295.zh.md.


### How can I publish the website to ApacheCon
First you need to write access right of [ApacheCon website]

Checking out the this repo
```
git@github.com:apache/acasia-website.git <source-directory>
```

After doing some modifications on the markdown files, you can use hugo command to generate the website from the source directory
```
cd <source-directory>
hugo -b https://asia.communityovercode.org/ -d <site-directory> -F
```


### How can I modify the content of the main page:

It's under `content/_index.md`

### How can I have translations:

Add new language to the `config.toml`:

```
[languages.zh]
languageName = "中文"
weight = 2
```

And create language specific version for each content file:

```
content/_index.md
content/_index.zh.md
content/cfp.md
content/cfp.zh.md
```

### How can I modify the menu?

For simple links, add the menu entry to the `config.toml`:

(Note: add it for all the active languages)

```
[[languages.en.menu.main]]
name = "t-shirt"
url = "https://s.apache.org/apache-tshirt"
weight = -110
```

The most page links of the menu are generated from the markdown files of content directory.
For a page, it's enough to add a menu entry to the markdown (For example `content/cfp.md`):

```
---
title: Call for Presentations
menu:
  main:
    weight: -300
---
...
...
```

You can add or remove the links from navigation bar by adding or removing this menu entry.
