from supabase import Client 
from connect_supabase import get_connect_supabase

supabase = get_connect_supabase()

response = supabase.table("alunos").select("*").execute()

print('select:',response)

response = (
    supabase.table("alunos")
    .insert({"nome": 'teste', "idade": 00})
    .execute()
)

print('insert:',response)

response = (
    supabase.table("alunos")
    .update({"nome": "new_test"})
    .eq('nome', 'teste')
    .execute()
)
 
print('update: ', response)

response = supabase.table('alunos').delete().eq('nome','teste').execute()
