# frozen_string_literal: true

require "cgi"

module HtmlUnescapeFilter
  # Decode HTML entities (e.g. &oslash; → ø) before | escape so names are not double-escaped.
  # Repeat until stable so double-encoded values like &amp;oslash; also become plain text.
  def html_unescape(input)
    return "" if input.nil?

    s = input.to_s
    10.times do
      t = CGI.unescapeHTML(s)
      break if t == s

      s = t
    end
    s
  end
end

Liquid::Template.register_filter(HtmlUnescapeFilter)
