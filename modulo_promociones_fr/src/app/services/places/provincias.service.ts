import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Provincias } from '../../interfaces/places/provincias.interface';

@Injectable({
  providedIn: 'root'
})
export class ProvinciasService {

  private baseUrl ='http://127.0.0.1:5012/api/ra/plcprov_endpoint';

  constructor(private http:HttpClient) { }
  
  getProvincias(): Observable<Provincias[]> {
    // Construir los parámetros de consulta
    let params = new HttpParams().set('type', 'ALL_PROVS');
    return this.http.get<Provincias[]>(this.baseUrl, { params: params });
  }

  getProvinciasXTecnologiasXTariffplanVariant(tecnologia: string, tariffplanvariant: number):Observable<Provincias[]>{
    let params = new HttpParams().set('type', 'SPECIFIC_PROVXTT')
    .set('TECNOLOGIA', tecnologia)
    .set('TARIFFPLANVARIANT', tariffplanvariant);
    return this.http.get<Provincias[]>(this.baseUrl, { params: params });
  }
}
