# frozen_string_literal: true

require "cgi"

module HtmlUnescapeFilter
  # Decode HTML entities (e.g. &oslash; → ø) before | escape so names are not double-escaped.
  def html_unescape(input)
    return "" if input.nil?

    CGI.unescapeHTML(input.to_s)
  end
end

Liquid::Template.register_filter(HtmlUnescapeFilter)
