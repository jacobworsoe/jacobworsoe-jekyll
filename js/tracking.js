var Tracking = {	
	// Track link clicks
	trackLinkClicks: function(e, eventCategory) {
		if (window["google_tag_manager"]) {
			if (e.target.tagName !== "A") return;

			var href = e.target.href;
			var clickText = e.target.innerText;

			window.dataLayer = window.dataLayer || [];

			dataLayer.push({
				event: "customLinkClick",
				eventCategory: eventCategory,
				clickText: clickText,
				href: href
			});
		}
	}
};
