function validateAndSanitizeHTML(htmlString, allowedTags) {
    const sanitizedHTML = DOMPurify.sanitize(htmlString, {
        ALLOWED_TAGS: allowedTags
    });

    if (sanitizedHTML === htmlString) {
        return true;
    } else {
        return false;
    }
}

const htmlString = newVal;

const allowedTags = ['p', 'h1', 'h2', 'h3', 'ul', 'ol', 'li', 'b', 'i', 'u', 's', 'strong', 'em', 'br', 'span']

const isValid = validateAndSanitizeHTML(htmlString, allowedTags);
this.quillValid = isValid;