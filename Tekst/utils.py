import bleach
import html
from bleach.css_sanitizer import CSSSanitizer

ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS = ['p', 'h1', 'h2', 'h3', 'ul', 'ol', 'li', 'b', 'i', 'u', 's', 'strong',
                                                'em', 'br', 'span']
ALLOWED_ATTRIBUTES = {'*': ['class', 'style'], }
ALLOWED_STYLES = ['color', 'background-color']
css_sanitizer = CSSSanitizer(allowed_css_properties=ALLOWED_STYLES)


def sanitize_and_escape(content):
    """
    Sanitizes the provided content and escapes HTML entities.
    :param content: String, content to be sanitized and escaped.
    :return: Escaped sanitized content.
    """
    unescaped_content = html.unescape(content)
    sanitized_content = bleach.clean(unescaped_content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                                     strip=True, css_sanitizer=css_sanitizer)

    return sanitized_content
