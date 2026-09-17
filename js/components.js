class SiteHeader extends HTMLElement {
  connectedCallback() {
    fetch(\'header.html\')
      .then(response => response.text())
      .then(html => {
        this.innerHTML = html;
        if(window.initHeaderJS) window.initHeaderJS();
      });
  }
}
class SiteFooter extends HTMLElement {
  connectedCallback() {
    fetch(\'footer.html\')
      .then(response => response.text())
      .then(html => {
        this.innerHTML = html;
      });
  }
}
customElements.define(\'site-header\', SiteHeader);
customElements.define(\'site-footer\', SiteFooter);
