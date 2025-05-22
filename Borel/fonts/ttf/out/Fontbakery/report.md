## FontBakery report

fontbakery version: 1.0.0







## Check results



<details><summary>[23] Borel-Regular.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Check if the axes match between the font and the Google Fonts version. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axes-match">googlefonts/axes_match</a></summary>
    <div>







* 💥 **ERROR** <p>Failed with BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.</p>
<pre><code>  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 152, in _get_check_dependencies
    val = bool(self._get(name, identity.iterargs, condition=True))
               ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 134, in _get
    return getattr(specific_thing, name)
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 371, in remote_style
    remote_styles = font.remote_styles
                    ^^^^^^^^^^^^^^^^^^
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 349, in remote_styles
    file_obj = download_file(dl_url)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/utils.py&quot;, line 344, in download_file
    raise BadCertificateSetupException(
    ...&lt;6 lines&gt;...
    )

</code></pre>
 [code: error]



</div>
</details>

<details>
    <summary>💥 <b>ERROR</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics-regressions">googlefonts/cjk_vertical_metrics_regressions</a></summary>
    <div>







* 💥 **ERROR** <p>Failed with BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.</p>
<pre><code>  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 152, in _get_check_dependencies
    val = bool(self._get(name, identity.iterargs, condition=True))
               ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 134, in _get
    return getattr(specific_thing, name)
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 381, in regular_remote_style
    remote_styles = font.remote_styles
                    ^^^^^^^^^^^^^^^^^^
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 349, in remote_styles
    file_obj = download_file(dl_url)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/utils.py&quot;, line 344, in download_file
    raise BadCertificateSetupException(
    ...&lt;6 lines&gt;...
    )

</code></pre>
 [code: error]



</div>
</details>

<details>
    <summary>💥 <b>ERROR</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics-regressions">googlefonts/vertical_metrics_regressions</a></summary>
    <div>







* 💥 **ERROR** <p>Failed with BadCertificateSetupException: You probably installed official Mac python from python.org but forgot to also install the certificates. There is a note in the installer Readme about that. Check the Python folder in the Applications directory, you should find a shell script to install the certificates.</p>
<pre><code>  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 152, in _get_check_dependencies
    val = bool(self._get(name, identity.iterargs, condition=True))
               ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 134, in _get
    return getattr(specific_thing, name)
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 381, in regular_remote_style
    remote_styles = font.remote_styles
                    ^^^^^^^^^^^^^^^^^^
  File &quot;/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/functools.py&quot;, line 1026, in __get__
    val = self.func(instance)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/checks/vendorspecific/googlefonts/conditions.py&quot;, line 349, in remote_styles
    file_obj = download_file(dl_url)
  File &quot;/Users/rosalie/env/lib/python3.13/site-packages/fontbakery/utils.py&quot;, line 344, in download_file
    raise BadCertificateSetupException(
    ...&lt;6 lines&gt;...
    )

</code></pre>
 [code: error]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1290, but got 1203 instead</p>
 [code: ascent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- uni031B
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x00AF (MACRON)


- 0x00D0 (LATIN CAPITAL LETTER ETH)


- 0x00DE (LATIN CAPITAL LETTER THORN)


- 0x00F0 (LATIN SMALL LETTER ETH)


- 0x00FE (LATIN SMALL LETTER THORN)


- 0x00FF (LATIN SMALL LETTER Y WITH DIAERESIS)


- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


- 0x0101 (LATIN SMALL LETTER A WITH MACRON)


- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


- 0x0105 (LATIN SMALL LETTER A WITH OGONEK)


- 91 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if uppercase glyphs are vertically centered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#caps-vertically-centered">caps_vertically_centered</a></summary>
    <div>







* ⚠️ **WARN** <p>Uppercase glyphs are not vertically centered in the em box.</p>
 [code: vertical-metrics-not-centered]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: f	Contours detected: 3	Expected: 1

- Glyph name: h	Contours detected: 2	Expected: 1

- Glyph name: j	Contours detected: 3	Expected: 2

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: l	Contours detected: 2	Expected: 1

- Glyph name: p	Contours detected: 1	Expected: 2

- Glyph name: y	Contours detected: 2	Expected: 1

- Glyph name: z	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: yacute	Contours detected: 3	Expected: 2

- 46 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* l.fina: L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt; has the same coordinates as a previous segment.

* l.fina.cv01: L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* l.fina.cv02: L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* l.fina.cv03: L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* l.isol: L&lt;&lt;129.0,538.0&gt;--&lt;129.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* l.isol.cv04: L&lt;&lt;92.0,538.0&gt;--&lt;92.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* ldot.fina: L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt; has the same coordinates as a previous segment.

* ldot.fina.cv01: L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* ldot.fina.cv02: L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* ldot.fina.cv03: L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt; has the same coordinates as a previous segment.

* 8 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- A.cv04

- A.cv05

- A.isol.cv04

- A.isol.cv05

- Aacute.isol.cv04

- Aacute.isol.cv05

- Abreve.isol.cv04

- Abreve.isol.cv05

- Acircumflex.isol.cv04

- Acircumflex.isol.cv05

- 193 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at . does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, tifinagh, duployan, hebrew, tai-le, syriac, coptic, math, old-permic, malayalam</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols
15 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* l.fina.cv01: L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt; -&gt; L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt;

* l.fina.cv02: L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt; -&gt; L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt;

* l.fina.cv03: L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt; -&gt; L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt;

* l.fina: L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt; -&gt; L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt;

* l.isol.cv04: L&lt;&lt;92.0,538.0&gt;--&lt;92.0,538.0&gt;&gt; -&gt; L&lt;&lt;92.0,538.0&gt;--&lt;92.0,538.0&gt;&gt;

* l.isol: L&lt;&lt;129.0,538.0&gt;--&lt;129.0,538.0&gt;&gt; -&gt; L&lt;&lt;129.0,538.0&gt;--&lt;129.0,538.0&gt;&gt;

* ldot.fina.cv01: L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt; -&gt; L&lt;&lt;120.0,538.0&gt;--&lt;120.0,538.0&gt;&gt;

* ldot.fina.cv02: L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt; -&gt; L&lt;&lt;51.0,538.0&gt;--&lt;51.0,538.0&gt;&gt;

* ldot.fina.cv03: L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt; -&gt; L&lt;&lt;24.0,538.0&gt;--&lt;24.0,538.0&gt;&gt;

* ldot.fina: L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt; -&gt; L&lt;&lt;118.0,537.0&gt;--&lt;118.0,537.0&gt;&gt;

* 29 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* v.fina.cv01: B&lt;&lt;809.5,322.0&gt;-&lt;783.0,317.0&gt;-&lt;751.0,314.0&gt;&gt;/L&lt;&lt;751.0,314.0&gt;--&lt;751.0,314.0&gt;&gt; = 5.355825042855143

* v.fina.cv02: B&lt;&lt;595.5,322.0&gt;-&lt;569.0,317.0&gt;-&lt;537.0,314.0&gt;&gt;/L&lt;&lt;537.0,314.0&gt;--&lt;537.0,314.0&gt;&gt; = 5.355825042855143

* v.fina.cv03: B&lt;&lt;716.5,322.0&gt;-&lt;690.0,317.0&gt;-&lt;658.0,314.0&gt;&gt;/L&lt;&lt;658.0,314.0&gt;--&lt;658.0,314.0&gt;&gt; = 5.355825042855143

* v.fina: B&lt;&lt;787.5,322.0&gt;-&lt;761.0,317.0&gt;-&lt;729.0,314.0&gt;&gt;/L&lt;&lt;729.0,314.0&gt;--&lt;729.0,314.0&gt;&gt; = 5.355825042855143

* v.isol: B&lt;&lt;715.5,322.0&gt;-&lt;689.0,317.0&gt;-&lt;657.0,314.0&gt;&gt;/L&lt;&lt;657.0,314.0&gt;--&lt;657.0,314.0&gt;&gt; = 5.355825042855143

* w.fina.cv01: B&lt;&lt;1036.5,322.0&gt;-&lt;1010.0,317.0&gt;-&lt;978.0,314.0&gt;&gt;/L&lt;&lt;978.0,314.0&gt;--&lt;978.0,314.0&gt;&gt; = 5.355825042855143

* w.fina.cv02: B&lt;&lt;822.5,322.0&gt;-&lt;796.0,317.0&gt;-&lt;764.0,314.0&gt;&gt;/L&lt;&lt;764.0,314.0&gt;--&lt;764.0,314.0&gt;&gt; = 5.355825042855143

* w.fina.cv03: B&lt;&lt;943.5,322.0&gt;-&lt;917.0,317.0&gt;-&lt;885.0,314.0&gt;&gt;/L&lt;&lt;885.0,314.0&gt;--&lt;885.0,314.0&gt;&gt; = 5.355825042855143

* w.fina: B&lt;&lt;1014.5,322.0&gt;-&lt;988.0,317.0&gt;-&lt;956.0,314.0&gt;&gt;/L&lt;&lt;956.0,314.0&gt;--&lt;956.0,314.0&gt;&gt; = 5.355825042855143

* w.isol: B&lt;&lt;942.5,322.0&gt;-&lt;916.0,317.0&gt;-&lt;884.0,314.0&gt;&gt;/L&lt;&lt;884.0,314.0&gt;--&lt;884.0,314.0&gt;&gt; = 5.355825042855143
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* M.cv05: L&lt;&lt;243.0,0.0&gt;--&lt;242.0,515.0&gt;&gt;

* M.isol.cv05: L&lt;&lt;243.0,0.0&gt;--&lt;242.0,515.0&gt;&gt;

* N.cv05: L&lt;&lt;243.0,0.0&gt;--&lt;242.0,515.0&gt;&gt;

* N.isol.cv05: L&lt;&lt;253.0,0.0&gt;--&lt;252.0,515.0&gt;&gt;

* Ntilde.isol.cv05: L&lt;&lt;253.0,0.0&gt;--&lt;252.0,515.0&gt;&gt;

* U.cv04: L&lt;&lt;779.0,722.0&gt;--&lt;780.0,150.0&gt;&gt;

* U.isol.cv04: L&lt;&lt;779.0,722.0&gt;--&lt;780.0,157.0&gt;&gt;

* Uacute.isol.cv04: L&lt;&lt;779.0,722.0&gt;--&lt;780.0,157.0&gt;&gt;

* Ucircumflex.isol.cv04: L&lt;&lt;779.0,722.0&gt;--&lt;780.0,157.0&gt;&gt;

* Udieresis.isol.cv04: L&lt;&lt;779.0,722.0&gt;--&lt;780.0,157.0&gt;&gt;

* 17 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> List all superfamily filepaths <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#superfamily-list">superfamily/list</a></summary>
    <div>







* ℹ️ **INFO** <p>.</p>
 [code: family-path]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>







* ℹ️ **INFO** <p>The family name &quot;Borel&quot; seems to be already in use.
Please visit <a href="http://namecheck.fontdata.com/?q=Borel">http://namecheck.fontdata.com/?q=Borel</a> for more info.</p>
 [code: name-collision]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#hinting-impact">hinting_impact</a></summary>
    <div>







* ℹ️ **INFO** <p>Hinting filesize impact:</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">Borel-Regular.ttf</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Dehinted Size</td>
<td align="right">188.8kb</td>
</tr>
<tr>
<td align="left">Hinted Size</td>
<td align="right">246.7kb</td>
</tr>
<tr>
<td align="left">Increase</td>
<td align="right">57.9kb</td>
</tr>
<tr>
<td align="left">Change</td>
<td align="right">30.6 %</td>
</tr>
</tbody>
</table>
 [code: size-impact]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#required-tables">required_tables</a></summary>
    <div>







* ℹ️ **INFO** <p>This font contains the following optional tables:</p>
<pre><code>- cvt 

- fpgm

- loca

- prep

- GPOS

- GSUB

- gasp
</code></pre>
 [code: optional-tables]





</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-article">googlefonts/description/has_article</a></summary>
    <div>







* ℹ️ **INFO** <p>This font doesn't have an ARTICLE.en_us.html file.</p>
 [code: missing-article]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-gasp">googlefonts/gasp</a></summary>
    <div>







* ℹ️ **INFO** <p>These are the ppm ranges declared on the gasp table:</p>
<p>PPM &lt;= 65535:
flag = 0x0F
- Use grid-fitting
- Use grayscale rendering
- Use gridfitting with ClearType symmetric smoothing
- Use smoothing along multiple axes with ClearType®</p>
 [code: ranges]



</div>
</details>
</div>
</details>

<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axis-order">googlefonts/STAT/axis_order</a></summary>
    <div>







* ℹ️ **INFO** <p>All of the fonts lack a STAT table.</p>
 [code: summary]





</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 3 | 0 | 3 | 11 | 104 | 7 | 108 | 0 | 
| 1% | 0% | 1% | 5% | 44% | 3% | 46% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* PASS
* DEBUG
