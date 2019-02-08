"""
HTMLGEN: Generador de HTML5 mediante JavaScript ES5.
Copyright 2019 Jesus Alan Ramirez Zatarain.
"""

class SIMBOLIZAR:
    """
    Para crear objetos de pares tipo-valor
    """
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor

class HTMLGEN:
    etiquetas: dict = {
        "DOCTYPE":    SIMBOLIZAR("HTMLTAG_DOCTYPE",    "DOCTYPE"),    # Defines the document type
        "a":          SIMBOLIZAR("HTMLTAG_A",          "A"),          # Defines a hyperlink
        "abbr":       SIMBOLIZAR("HTMLTAG_ABBR",       "ABBR"),       # Defines an abbreviation or an acronym
        "acronym":    SIMBOLIZAR("DPRCATD_ACRONYM",    "ACRONYM"),    # FIXME Not supported in HTML5. Use <abbr> instead. Defines an acronym
        "address":    SIMBOLIZAR("HTMLTAG_ADDRESS",    "ADDRESS"),    # Defines contact information for the author/owner of a document
        "applet":     SIMBOLIZAR("DPRCATD_APPLET",     "APPLET"),     # FIXME Not supported in HTML5. Use <embed> or <object> instead. Defines an embedded applet
        "area":       SIMBOLIZAR("HTMLTAG_AREA",       "AREA"),       # Defines an area inside an image-map
        "article":    SIMBOLIZAR("HTML5NW_ARTICLE",    "ARTICLE"),    # XXX Defines an article
        "aside":      SIMBOLIZAR("HTML5NW_ASIDE",      "ASIDE"),      # XXX Defines content aside from the page content
        "audio":      SIMBOLIZAR("HTML5NW_AUDIO",      "AUDIO"),      # XXX Defines sound content
        "b":          SIMBOLIZAR("HTMLTAG_B",          "B"),          # Defines bold text
        "base":       SIMBOLIZAR("HTMLTAG_BASE",       "BASE"),       # Specifies the base URL/target for all relative URLs in a document
        "basefont":   SIMBOLIZAR("DPRCATD_BASEFONT",   "BASEFONT"),   # FIXME Not supported in HTML5. Use CSS instead. Specifies a default color, size, and font for all text in a document
        "bdi":        SIMBOLIZAR("HTML5NW_BDI",        "BDI"),        # XXX Isolates a part of text that might be formatted in a different direction from other text outside it
        "bdo":        SIMBOLIZAR("HTMLTAG_BDO",        "BDO"),        # Overrides the current text direction
        "big":        SIMBOLIZAR("DPRCATD_BIG",        "BIG"),        # FIXME Not supported in HTML5. Use CSS instead. Defines big text
        "blockquote": SIMBOLIZAR("HTMLTAG_BLOCKQUOTE", "BLOCKQUOTE"), # Defines a section that is quoted from another source
        "body":       SIMBOLIZAR("HTMLTAG_BODY",       "BODY"),       # Defines the document's body
        "br":         SIMBOLIZAR("HTMLTAG_BR",         "BR"),         # Defines a single line break
        "button":     SIMBOLIZAR("HTMLTAG_BUTTON",     "BUTTON"),     # Defines a clickable button
        "canvas":     SIMBOLIZAR("HTML5NW_CANVAS",     "CANVAS"),     # XXX Used to draw graphics, on the fly, via scripting (usually JavaScript)
        "caption":    SIMBOLIZAR("HTMLTAG_CAPTION",    "CAPTION"),    # Defines a table caption
        "center":     SIMBOLIZAR("DPRCATD_CENTER",     "CENTER"),     # FIXME Not supported in HTML5. Use CSS instead. Defines centered text
        "cite":       SIMBOLIZAR("HTMLTAG_CITE",       "CITE"),       # Defines the title of a work
        "code":       SIMBOLIZAR("HTMLTAG_CODE",       "CODE"),       # Defines a piece of computer code
        "col":        SIMBOLIZAR("HTMLTAG_COL",        "COL"),        # Specifies column properties for each column within a <colgroup> element 
        "colgroup":   SIMBOLIZAR("HTMLTAG_COLGROUP",   "COLGROUP"),   # Specifies a group of one or more columns in a table for formatting
        "data":       SIMBOLIZAR("HTML5NW_DATA",       "DATA"),       # XXX Links the given content with a machine-readable translation
        "datalist":   SIMBOLIZAR("HTML5NW_DATALIST",   "DATALIST"),   # XXX Specifies a list of pre-defined options for input controls
        "dd":         SIMBOLIZAR("HTMLTAG_DD",         "DD"),         # Defines a description/value of a term in a description list
        "del":        SIMBOLIZAR("HTMLTAG_DEL",        "DEL"),        # Defines text that has been deleted from a document
        "details":    SIMBOLIZAR("HTML5NW_DETAILS",    "DETAILS"),    # XXX Defines additional details that the user can view or hide
        "dfn":        SIMBOLIZAR("HTMLTAG_DFN",        "DFN"),        # Represents the defining instance of a term
        "dialog":     SIMBOLIZAR("HTML5NW_DIALOG",     "DIALOG"),     # XXX Defines a dialog box or window
        "dir":        SIMBOLIZAR("DPRCATD_DIR",        "DIR"),        # FIXME Not supported in HTML5. Use <ul> instead. Defines a directory list
        "div":        SIMBOLIZAR("HTMLTAG_DIV",        "DIV"),        # Defines a section in a document
        "dl":         SIMBOLIZAR("HTMLTAG_DL",         "DL"),         # Defines a description list
        "dt":         SIMBOLIZAR("HTMLTAG_DT",         "DT"),         # Defines a term/name in a description list
        "em":         SIMBOLIZAR("HTMLTAG_EM",         "EM"),         # Defines emphasized text 
        "embed":      SIMBOLIZAR("HTML5NW_EMBED",      "EMBED"),      # XXX Defines a container for an external (non-HTML) application
        "fieldset":   SIMBOLIZAR("HTMLTAG_FIELDSET",   "FIELDSET"),   # Groups related elements in a form
        "figcaption": SIMBOLIZAR("HTML5NW_FIGCAPTION", "FIGCAPTION"), # XXX Defines a caption for a <figure> element
        "figure":     SIMBOLIZAR("HTML5NW_FIGURE",     "FIGURE"),     # XXX Specifies self-contained content
        "font":       SIMBOLIZAR("DPRCATD_FONT",       "FONT"),       # FIXME Not supported in HTML5. Use CSS instead. Defines font, color, and size for text
        "footer":     SIMBOLIZAR("HTML5NW_FOOTER",     "FOOTER"),     # XXX Defines a footer for a document or section
        "form":       SIMBOLIZAR("HTMLTAG_FORM",       "FORM"),       # Defines an HTML form for user input
        "frame":      SIMBOLIZAR("DPRCATD_FRAME",      "FRAME"),      # FIXME Not supported in HTML5. Defines a window (a frame) in a frameset
        "frameset":   SIMBOLIZAR("DPRCATD_FRAMESET",   "FRAMESET"),   # FIXME Not supported in HTML5. Defines a set of frames
        "h1":         SIMBOLIZAR("HTMLTAG_H1",         "H1"),         # Defines HTML headings level 1
        "h2":         SIMBOLIZAR("HTMLTAG_H2",         "H2"),         # Defines HTML headings level 2
        "h3":         SIMBOLIZAR("HTMLTAG_H3",         "H3"),         # Defines HTML headings level 3
        "h4":         SIMBOLIZAR("HTMLTAG_H4",         "H4"),         # Defines HTML headings level 4
        "h5":         SIMBOLIZAR("HTMLTAG_H5",         "H5"),         # Defines HTML headings level 5
        "h6":         SIMBOLIZAR("HTMLTAG_H6",         "H6"),         # Defines HTML headings level 6
        "head":       SIMBOLIZAR("HTMLTAG_HEAD",       "HEAD"),       # Defines information about the document
        "header":     SIMBOLIZAR("HTML5NW_HEADER",     "HEADER"),     # XXX Defines a header for a document or section
        "hr":         SIMBOLIZAR("HTMLTAG_HR",         "HR"),         # Defines a thematic change in the content
        "html":       SIMBOLIZAR("HTMLTAG_HTML",       "HTML"),       # Defines the root of an HTML document
        "i":          SIMBOLIZAR("HTMLTAG_I",          "I"),          # Defines a part of text in an alternate voice or mood
        "iframe":     SIMBOLIZAR("HTMLTAG_IFRAME",     "IFRAME"),     # Defines an inline frame
        "img":        SIMBOLIZAR("HTMLTAG_IMG",        "IMG"),        # Defines an image
        "input":      SIMBOLIZAR("HTMLTAG_INPUT",      "INPUT"),      # Defines an input control
        "ins":        SIMBOLIZAR("HTMLTAG_INS",        "INS"),        # Defines a text that has been inserted into a document
        "kbd":        SIMBOLIZAR("HTMLTAG_KBD",        "KBD"),        # Defines keyboard input
        "label":      SIMBOLIZAR("HTMLTAG_LABEL",      "LABEL"),      # Defines a label for an <input> element
        "legend":     SIMBOLIZAR("HTMLTAG_LEGEND",     "LEGEND"),     # Defines a caption for a <fieldset> element
        "li":         SIMBOLIZAR("HTMLTAG_LI",         "LI"),         # Defines a list item
        "link":       SIMBOLIZAR("HTMLTAG_LINK",       "LINK"),       # Defines the relationship between a document and an external resource (most used to link to style sheets)
        "main":       SIMBOLIZAR("HTML5NW_MAIN",       "MAIN"),       # XXX Specifies the main content of a document
        "map":        SIMBOLIZAR("HTMLTAG_MAP",        "MAP"),        # Defines a client-side image-map
        "mark":       SIMBOLIZAR("HTML5NW_MARK",       "MARK"),       # XXX Defines marked/highlighted text
        "meta":       SIMBOLIZAR("HTMLTAG_META",       "META"),       # Defines metadata about an HTML document
        "meter":      SIMBOLIZAR("HTML5NW_METER",      "METER"),      # XXX Defines a scalar measurement within a known range (a gauge)
        "nav":        SIMBOLIZAR("HTML5NW_NAV",        "NAV"),        # XXX Defines navigation links
        "noframes":   SIMBOLIZAR("DPRCATD_NOFRAMES",   "NOFRAMES"),   # FIXME Not supported in HTML5. Defines an alternate content for users that do not support frames
        "noscript":   SIMBOLIZAR("HTMLTAG_NOSCRIPT",   "NOSCRIPT"),   # Defines an alternate content for users that do not support client-side scripts
        "object":     SIMBOLIZAR("HTMLTAG_OBJECT",     "OBJECT"),     # Defines an embedded object
        "ol":         SIMBOLIZAR("HTMLTAG_OL",         "OL"),         # Defines an ordered list
        "optgroup":   SIMBOLIZAR("HTMLTAG_OPTGROUP",   "OPTGROUP"),   # Defines a group of related options in a drop-down list
        "option":     SIMBOLIZAR("HTMLTAG_OPTION",     "OPTION"),     # Defines an option in a drop-down list
        "output":     SIMBOLIZAR("HTML5NW_OUTPUT",     "OUTPUT"),     # XXX Defines the result of a calculation
        "p":          SIMBOLIZAR("HTMLTAG_P",          "P"),          # Defines a paragraph
        "param":      SIMBOLIZAR("HTMLTAG_PARAM",      "PARAM"),      # Defines a parameter for an object
        "picture":    SIMBOLIZAR("HTML5NW_PICTURE",    "PICTURE"),    # XXX Defines a container for multiple image resources
        "pre":        SIMBOLIZAR("HTMLTAG_PRE",        "PRE"),        # Defines preformatted text
        "progress":   SIMBOLIZAR("HTML5NW_PROGRESS",   "PROGRESS"),   # XXX Represents the progress of a task
        "q":          SIMBOLIZAR("HTMLTAG_Q",          "Q"),          # Defines a short quotation
        "rp":         SIMBOLIZAR("HTML5NW_RP",         "RP"),         # XXX Defines what to show in browsers that do not support ruby annotations
        "rt":         SIMBOLIZAR("HTML5NW_RT",         "RT"),         # XXX Defines an explanation/pronunciation of characters (for East Asian typography)
        "ruby":       SIMBOLIZAR("HTML5NW_RUBY",       "RUBY"),       # XXX Defines a ruby annotation (for East Asian typography)
        "s":          SIMBOLIZAR("HTMLTAG_S",          "S"),          # Defines text that is no longer correct
        "samp":       SIMBOLIZAR("HTMLTAG_SAMP",       "SAMP"),       # Defines sample output from a computer program
        "script":     SIMBOLIZAR("HTMLTAG_SCRIPT",     "SCRIPT"),     # Defines a client-side script
        "section":    SIMBOLIZAR("HTML5NW_SECTION",    "SECTION"),    # XXX Defines a section in a document
        "select":     SIMBOLIZAR("HTMLTAG_SELECT",     "SELECT"),     # Defines a drop-down list
        "small":      SIMBOLIZAR("HTMLTAG_SMALL",      "SMALL"),      # Defines smaller text
        "source":     SIMBOLIZAR("HTML5NW_SOURCE",     "SOURCE"),     # XXX Defines multiple media resources for media elements (<video> and <audio>)
        "span":       SIMBOLIZAR("HTMLTAG_SPAN",       "SPAN"),       # Defines a section in a document
        "strike":     SIMBOLIZAR("DPRCATD_STRIKE",     "STRIKE"),     # FIXME Not supported in HTML5. Use <del> or <s> instead. Defines strikethrough text
        "strong":     SIMBOLIZAR("HTMLTAG_STRONG",     "STRONG"),     # Defines important text
        "style":      SIMBOLIZAR("HTMLTAG_STYLE",      "STYLE"),      # Defines style information for a document
        "sub":        SIMBOLIZAR("HTMLTAG_SUB",        "SUB"),        # Defines subscripted text
        "summary":    SIMBOLIZAR("HTML5NW_SUMMARY",    "SUMMARY"),    # XXX Defines a visible heading for a <details> element
        "sup":        SIMBOLIZAR("HTMLTAG_SUP",        "SUP"),        # Defines superscripted text
        "svg":        SIMBOLIZAR("HTMLTAG_SVG",        "SVG"),        # Defines a container for SVG graphics
        "table":      SIMBOLIZAR("HTMLTAG_TABLE",      "TABLE"),      # Defines a table
        "tbody":      SIMBOLIZAR("HTMLTAG_TBODY",      "TBODY"),      # Groups the body content in a table
        "td":         SIMBOLIZAR("HTMLTAG_TD",         "TD"),         # Defines a cell in a table
        "template":   SIMBOLIZAR("HTML5NW_TEMPLATE",   "TEMPLATE"),   # XXX Defines a template
        "textarea":   SIMBOLIZAR("HTMLTAG_TEXTAREA",   "TEXTAREA"),   # Defines a multiline input control (text area)
        "tfoot":      SIMBOLIZAR("HTMLTAG_TFOOT",      "TFOOT"),      # Groups the footer content in a table
        "th":         SIMBOLIZAR("HTMLTAG_TH",         "TH"),         # Defines a header cell in a table
        "thead":      SIMBOLIZAR("HTMLTAG_THEAD",      "THEAD"),      # Groups the header content in a table
        "time":       SIMBOLIZAR("HTML5NW_TIME",       "TIME"),       # XXX Defines a date/time
        "title":      SIMBOLIZAR("HTMLTAG_TITLE",      "TITLE"),      # Defines a title for the document
        "tr":         SIMBOLIZAR("HTMLTAG_TR",         "TR"),         # Defines a row in a table
        "track":      SIMBOLIZAR("HTML5NW_TRACK",      "TRACK"),      # XXX Defines text tracks for media elements (<video> and <audio>)
        "tt":         SIMBOLIZAR("DPRCATD_TT",         "TT"),         # FIXME Not supported in HTML5. Use CSS instead. Defines teletype text
        "u":          SIMBOLIZAR("HTMLTAG_U",          "U"),          # Defines text that should be stylistically different from normal text
        "ul":         SIMBOLIZAR("HTMLTAG_UL",         "UL"),         # Defines an unordered list
        "var":        SIMBOLIZAR("HTMLTAG_VAR",        "VAR"),        # Defines a variable
        "video":      SIMBOLIZAR("HTML5NW_VIDEO",      "VIDEO"),      # XXX Defines a video or movie
        "wbr":        SIMBOLIZAR("HTML5NW_WBR",        "WBR"),        # XXX Defines a possible line-break
    }

    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0
        self.caracterActual = self.texto[self.posicion]
        self.caracterAnterior = None
        self.columna = 0
        self.linea = 1

    def cargarSiguenteSimbolo(self):
        while self.caracterActual is not None:
            if self.caracterActual.isspace():
                if self.caracterActual == "\n":
                    self.linea += 1
                while self.caracterActual is not None and self.caracterActual.isspace():
                    self.posicion += 1
                    self.columna += 1
                    if self.posicion > len(self.texto) - 1:
                        self.caracterActual = None
                    else:
                        self.caracterAnterior = self.texto[self.posicion-1]
                        self.caracterActual = self.texto[self.posicion]
                self.columna = 1
                continue
            elif self.caracterActual.isalpha():
                cadenaEncontrada = ""
                while self.caracterActual is not None and self.caracterActual.isalnum():
                    cadenaEncontrada += self.caracterActual
                    self.posicion += 1
                    self.columna += 1
                    if self.posicion > len(self.texto) - 1:
                        self.caracterActual = None
                    else:
                        self.caracterActual = self.texto[self.posicion]
                        self.caracterAnterior = self.texto[self.posicion-1]
            raise Exception("Caracter no reconocido: " + self.caracterActual)
        return SIMBOLIZAR("FIN", None)