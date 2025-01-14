from users import get_user_credentials
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    creds = get_user_credentials(user_id=user_id)

