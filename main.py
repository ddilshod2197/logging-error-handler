import logging

# Log faylini yaratish
logging.basicConfig(filename='log.txt', level=logging.ERROR)

def toza_kod():
    try:
        # Toza kodni bajarish
        1 / 0
    except ZeroDivisionError:
        # Xatoni log fayliga yozish
        logging.error('Toza kodda bo\'lishi mumkin bo\'lgan xato: 0 ga bo\'lishni harakat qilish')

def main():
    toza_kod()

if __name__ == '__main__':
    main()
```

```python
import logging

# Log faylini yaratish
logging.basicConfig(filename='log.txt', level=logging.ERROR)

def xato_kod():
    try:
        # Xato kodni bajarish
        1 / 0
    except ZeroDivisionError:
        # Xatoni log fayliga yozish
        logging.error('Xato kodda bo\'lishi mumkin bo\'lgan xato: 0 ga bo\'lishni harakat qilish')

def main():
    xato_kod()

if __name__ == '__main__':
    main()
