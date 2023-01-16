from django.db import models

class EntryManager(models.Manager):
    """ procedure for entry """

    def front_page_entry(self):
        return self.filter(
            public=True,
            cover=True,
        ).order_by('-created').first()
    
    def entries_in_home(self):
        # devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]
    
    def entries_recent(self):
        # devuelve las ultimas 4 entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:4]

    def search_entry(self, kword, category):
        # To search for entries by category or keyword
        if len(category) > 0:
            return self.filter(
                category__short_name=category,
                tittle__icontains=kword,
                public=True,
            ).order_by('-created')
        
        else:
            return self.filter(
                tittle__icontains=kword,
                public=True,
            ).order_by('-created')
