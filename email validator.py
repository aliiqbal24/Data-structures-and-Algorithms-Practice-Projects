class EmailValidator:
    # List of acceptable top level domains
    ALLOWED_TLDS = {'.com', '.ca', '.org', '.net', '.gov', '.edu'}

    # List of uacceptable second level domains
    FORBIDDEN_DOMAINS = {
        'scam', 'spam', 'fakeemail', 'trashmail',
        'pleasenotspam', 'therealtaylorswift', 'sendmoney'}

    def local_part_validator(local):
        # List of acceptable characters in local part
        valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-"
        return all(char in valid_chars for char in local)

    def validate_email(email):
        # Checks that there is exactly 1 '@' symbol
        if email.count('@') != 1:
            return "Invalid"
        
        # Splits each email into a local part and domain part
        local, domain = email.split('@')
        
        # Validates the local part
        if not EmailValidator.local_part_validator(local):
            return f"Invalid"
        
        # Validates the domain part by checking if it contains a period)
        if '.' not in domain:
            return "Invalid"
        
        # Splits the domain into second-level domain and TLD
        period_index = domain.rfind('.')
        second_level = domain[:period_index]
        tld = domain[period_index:]
        
        # Validates the Top level domain
        if tld not in EmailValidator.ALLOWED_TLDS:
            return f"Invalid"
        
        # Checks if the second-level domain is in forbidden list
        if second_level in EmailValidator.FORBIDDEN_DOMAINS:
            return f"Forbidden"
        
        # If no check returns invalid or forbidden, the email is valid
        return "Valid"

def main():
    # Takes the input and stores the email addresses in a list, spliting them up aat the spaces of the input
    emails = list(input().split())

    # Runs each email through the validator
    for email in emails:
        print(EmailValidator.validate_email(email))

if __name__ == "__main__":
    main()