int main(int argc, char *argv[])
{
   FILE *FPTR;

   FPTR=fopen("program.txt","a+");
   if(FPTR==NULL){
      printf("Error!");
      exit(1);
   }
   fprintf(FPTR,"program is written");
   printf("program is written in program.txt");
   fclose(FPTR);
   return 0;
}
