d a t a [ ’ p l _ p u b d a t e ’ ] = pd . t o _ d a t e t i m e ( d a t a [ ’
p l _ p u b d a t e ’ ] )
# S o r t i n g t h e d at a
s o r t e d D a t a = d a t a . s o r t _ v a l u e s ( by = [ ’ pl_name ’ , ’
p l _ p u b d a t e ’ ] , a s c e n d i n g = [ 1 , 0 ] , i n p l a c e = F al s e ,
n a _ p o s i t i o n = ’ l a s t ’ )
# S t o r e t h e d u p l i c a t e s b e f o r e r em o vi n g them
d u p l i c a t e s = pd . DataF rame ( c ol um n s = l i s t ( d a t a .
c ol um n s ) )
mask = s o r t e d D a t a . d u p l i c a t e d ( s u b s e t = ’ pl_name ’ ,
kee p = ’ f i r s t ’ )
d f _ k e e p = s o r t e d D a t a . l o c [ ~ mask ]
d u p l i c a t e s = d u p l i c a t e s . a p pe n d ( s o r t e d D a t a . l o c [ mask
] )
# D r o p pi n g t h e d u p l i c a t e s
deDupedData = s o r t e d D a t a . d r o p _ d u p l i c a t e s ( s u b s e t =
’ pl_name ’ , kee p = ’ f i r s t ’ , i n p l a c e = F al s e ,
i g n o r e _ i n d e x =T r ue )