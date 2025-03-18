I’m glad you’re digging deeper into customizing Stoplight Elements! The `<elements-api>` tag is the core component of Stoplight Elements, and its options/parameters let you control its behavior, layout, and appearance. Since you’re focused on layout and themes, knowing all the available options will help you tailor it exactly to your needs. Let’s get you the full list and point you to the best resources.

---

### Where to Find All `<elements-api>` Options/Parameters
Stoplight Elements’ official documentation provides the complete list of configuration options for the `<elements-api>` tag. Here’s how to access it:

#### Primary Resource
- **Stoplight Elements Configuration Options Docs**:
  - URL: [https://meta.stoplight.io/docs/elements/b074dc47b2826-elements-configuration-options](https://meta.stoplight.io/docs/elements/b074dc47b2826-elements-configuration-options)
  - **What You’ll Find**: A detailed table of all attributes (parameters) you can set on the `<elements-api>` tag, including descriptions, types, and default values.
  - **Access**: Publicly available, no login required as of March 18, 2025.

#### Alternative Sources
- **GitHub Repository**: [https://github.com/stoplightio/elements](https://github.com/stoplightio/elements)
  - Check the `docs/` folder or `README.md` for usage examples and additional notes.
  - Look at `/examples/` for practical implementations (e.g., `bootstrap/index.html`).
- **Stoplight Elements Main Page**: [https://stoplight.io/open-source/elements](https://stoplight.io/open-source/elements)
  - Links to docs and demos, though the configuration page above is more specific.

---

### Full List of `<elements-api>` Options (As of v7.16.0+)
Here’s a comprehensive rundown of the options based on the official docs (I’ll summarize key ones you’re likely interested in for layout and themes, but the linked page has the exhaustive list). These are HTML attributes you can add to the `<elements-api>` tag in your `static/docs.html`.

#### Core Options
- **`apiDescriptionUrl`**:
  - Type: `string`
  - Description: URL to your OpenAPI spec (e.g., `/openapi.json`).
  - Example: `apiDescriptionUrl="/openapi.json"`
  - Required: Yes (unless using `apiDescriptionDocument`).

- **`apiDescriptionDocument`**:
  - Type: `string` or `object`
  - Description: Inline OpenAPI spec as text or JS object (alternative to URL).
  - Example: `<script>document.getElementById('docs').apiDescriptionDocument = '{"openapi": "3.1.0", ...}';</script>`

#### Layout-Related Options
- **`layout`**:
  - Type: `string`
  - Values: `"sidebar"`, `"stacked"`, `"row"`
  - Default: `"sidebar"`
  - Description: Sets the overall layout (your current choice is `sidebar`).
  - Example: `layout="stacked"`

- **`hideTryIt`**:
  - Type: `boolean`
  - Default: `false`
  - Description: Hides the try-it pane (right side).
  - Example: `hideTryIt="true"`

- **`tryItCredentialsPolicy`**:
  - Type: `string`
  - Values: `"omit"`, `"include"`, `"same-origin"`
  - Default: `"omit"`
  - Description: Controls CORS credential behavior in the try-it pane.
  - Example: `tryItCredentialsPolicy="include"`

#### Theme-Related Options
- **`theme`**:
  - Type: `string`
  - Values: `"light"`, `"dark"`
  - Default: `"light"`
  - Description: Switches between light and dark base themes (overridable with CSS).
  - Example: `theme="dark"` (Note: Not officially listed but commonly supported; test it).

- **`logo`**:
  - Type: `string`
  - Description: URL to a custom logo in the header.
  - Example: `logo="/static/my-logo.png"`

- **`fontSize`**:
  - Type: `string`
  - Values: `"small"`, `"medium"`, `"large"`
  - Default: `"medium"`
  - Description: Adjusts base font size (CSS can override further).
  - Example: `fontSize="large"`

#### Navigation and Behavior
- **`router`**:
  - Type: `string`
  - Values: `"hash"`, `"memory"`, `"history"`
  - Default: `"hash"`
  - Description: Controls URL navigation behavior.
  - Example: `router="memory"`

- **`basePath`**:
  - Type: `string`
  - Description: Base path for routing (useful with `history` router).
  - Example: `basePath="/docs"`

- **`hideInternal`**:
  - Type: `boolean`
  - Default: `false`
  - Description: Hides endpoints marked `x-internal` in OpenAPI.
  - Example: `hideInternal="true"`

#### Other Useful Options
- **`hideExport`**:
  - Type: `boolean`
  - Default: `false`
  - Description: Hides the export button.
  - Example: `hideExport="true"`

- **`hideMocking`**:
  - Type: `boolean`
  - Default: `false`
  - Description: Disables mock server options.
  - Example: `hideMocking="true"`

- **`tryItCorsProxy`**:
  - Type: `string`
  - Description: URL to a CORS proxy for try-it requests.
  - Example: `tryItCorsProxy="https://my-proxy.com"`

---

### Applying to Your Setup
#### Example with Layout and Theme
Update `static/docs.html`:
```html
<elements-api
  apiDescriptionUrl="/openapi.json"
  router="hash"
  layout="sidebar"
  theme="dark"  <!-- Try dark theme -->
  fontSize="large"  <!-- Bigger text -->
  hideTryIt="false"
/>
```
- **Test**: See how `theme="dark"` and `fontSize="large"` look.

#### Combine with CSS
Your `styles.css` can override or complement these:
```css
elements-api::part(sidebar) {
  width: 20%;
  background-color: #2c3e50; /* Darker for dark theme */
}
elements-api::part(try-it) {
  width: 60%; /* More result space */
  background-color: #34495e; /* Matches dark theme */
}
```

---

### Why This Matters for You
- **Layout**: Options like `layout`, `hideTryIt`, and CSS `::part` give you control over pane visibility and size.
- **Themes**: `theme`, `fontSize`, and CSS variables in `styles.min.css` (e.g., `--sl-color-primary`) let you craft a unique look.

---

### Next Steps
- **Visit the Docs**: Hit the [Configuration Options page](https://meta.stoplight.io/docs/elements/b074dc47b2826-elements-configuration-options) for the latest list—it’s the definitive source.
- **Experiment**: Try `layout="stacked"` or `theme="dark"` in `docs.html`.
- **Ask**: Want a specific layout (e.g., “minimal sidebar”) or theme (e.g., “green accents”)? I can craft examples!
- **Share**: How’s it going—any options you’re excited to try?

You’ve got all the tools now—Stoplight Elements is your canvas! What customization are you thinking of next?