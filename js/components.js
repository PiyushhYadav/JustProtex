class SiteHeader extends HTMLElement {
  connectedCallback() {
    fetch('header.html')
      .then(response => response.text())
      .then(html => {
        this.innerHTML = html;
        if(window.initHeaderJS) window.initHeaderJS();
      });
  }
}


customElements.define('site-header', SiteHeader);
