# How to Use Borel

Borel is an open source font, which means you have the liberty to use it in all your projects, including commercial ones, completely free of charge.

## Downloading Fonts

1. **From the [release package](https://github.com/RosaWagner/Borel/releases)**: click the `fonts.zip` file from the last release to download it.

2. **From the "fonts" directory**: 
   - [Borel](../Borel/fonts/ttf/)
   - [Borel Guide](../BorelGuides/fonts/ttf/) 

## Installing Fonts
### Mac

1. **Open Font Book**: Font Book is the default font management tool on macOS. You can find it by going to the "Applications" folder or by using Spotlight search.

2. **Install the font**: Double-click the downloaded font file, and Font Book will open. Click the "Install Font" button in the font preview window. Alternatively, you can drag and drop the font file into the Font Book window.

3. **Verify installation**: Once installed, you can find the font listed in Font Book. You can also use the font in various applications on your Mac, such as text editors or design software.

### Windows:

1. **Install the font**: Double-click each font file. A preview window will open. Click the "Install" button at the top of the preview window. Alternatively, you can right-click the font file and select "Install" from the context menu.

2. **Verify installation**: After installation, the font will be available for use in applications. You can confirm the installation by checking the font list in programs like word processors, graphic design software, or the Windows Fonts folder located in the Control Panel.

**If an error message pops up during installation, please report it by [opening an issue](https://github.com/RosaWagner/Borel/issues) in this repository. To do so, follow the link and click the green button "New issue", don't forget to join a screenshot of the error message.**

## Activating Contextual Alternates in Fonts

The use of Borel depends greatly on "contextual alternatives", which is an option that allows the font to choose the appropriate letter form based on the surrounding letters and thus connect them.

This option is activated by default in many desktop and web application but not in Micsoft Office apps. If the letters don't connect, follow these steps below.

### Mac

1. Select the text.
2. Go to `Format` > `Font` or `Show Fonts`.
3. Look for `Typography` or `Advanced` section.
4. Check the `Use Contextual Alternates` box.

### Windows

1. Select the text.
2. Right-click and choose `Font` or `Font Settings`.
3. Go to `Advanced` tab.
4. Check the `Use Contextual Alternates` box.

## Borel Guide: Color and Variable fonts

- Borel Guides is a *Color Font*. This is a special format that allows a font to contain and render color palettes on the screen. If you don't see the colors in your text editor, it means your software doesn't support this technology. 

- Borel Guides is also a *variable* font. It's a format that lets you modify the font on different axes, such as width and weight. It's advisable not to use the [variable font](./BorelGuides/fonts/variable/) in your text editor software, as it's intended for the web. Use the [static fonts](./BorelGuides/fonts/ttf/) instead. Many programs support colored fonts *or* variable fonts, but not colored *and* variable fonts together.

## Using Borel and Borel Guide together

To use Borel and Borel Guides together, you need to overlay two different text frames. 

In MS Word, you can use Borel to write the main text. Then you would have to create an text box for Borel Guides:

- go to the menu: `insert` > `text box` > `simple text box`. This text zone will works like an image frame, i.e. you can use the small anchor to tell it to place itself "behind the text" on the main page. You can also remove borders etc.

- Line spacing is already set for common text editors such as Word, Page or TextEdit. Nevertheless, make sure that Borel and Borel Guide have the same value so they can overlap perfectly. Set the linespacing to `1` for a better experience.
 
- In Indesign, you'll need to use double line spacing to allow the grid to nest perfectly from one line to the next. For example, ff you choose a `24 pt` font size, choose `48 pt` line spacing.

