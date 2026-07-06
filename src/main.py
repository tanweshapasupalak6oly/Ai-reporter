"""AI Weekly Reporter entry point."""

from datetime import datetime


def main():
    print('=' * 60)
    print('AI Weekly Reporter')
    print(f'Started: {datetime.utcnow().isoformat()} UTC')
    print('Project scaffold created successfully.')
    print('Next modules will fetch news, generate the report, create a Google Doc, and email it.')
    print('=' * 60)


if __name__ == '__main__':
    main()
